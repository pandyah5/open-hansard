# For calling the API
import requests

# For annotating the summaries with dates
import datetime

# For calling the llama3 model
import ollama

# Read the XML content and parse it
from xml.etree import ElementTree as ET

# Import helper functions
from conversation import Speaker, Dialogue, Collection
from availability import get_parliament_and_session_id, get_new_debate

# For DEBUG
import warnings
DEBUG = 0

# Get the parliament and session number using get_parliament_and_session_id
parliament_num, session_num = get_parliament_and_session_id()
if get_new_debate(parliament_num, session_num) == False:
    print(">>> INFO: No new debate available")
    exit()

debate_num = ""
with open("last-retrieved.txt", "r") as file:
        print(">>> INFO: New debate available:", debate_num)
        last_retrieved_data = file.read().split('-')
        debate_num = last_retrieved_data[2]
        file.close()

def call_api():
    # Get the new debate URL
    url = ""
    with open("new-debate.txt", "r") as file:
        url = file.read()
        file.close()
    
    response = requests.get(url)
    if response.status_code == 200:
        text_data = response.text
        return text_data
    else:
        print(">>> FATAL: Failed to call the API.", url, response.status_code)
        exit()

text_data = call_api()

# Filter the first line of XML content
xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
text_data = text_data[text_data.find(xml_declaration):]

# For each SubjectOfBusiness element within HansardBody, print the PersonSpeaking
def generate_dialogue_summary(xml_content):
    list_of_collections = []
    root = ET.fromstring(xml_content).find('HansardBody')
    word_counter = 0
    
    for subject_of_business in root.iter('SubjectOfBusiness'):
        for content in subject_of_business.iter('SubjectOfBusinessContent'):
            for intervention in content.iter('Intervention'):
                if DEBUG:
                    print("\n\n### New Intervention ###")
                collection = Collection('')
                source = Speaker('', '')
                for speaker in intervention.iter('PersonSpeaking'):
                    flag = 0
                    
                    if DEBUG:
                        print("### Speaker ###")
                    
                    for Affiliation in speaker.iter('Affiliation'):
                        if flag == 1:
                            assert False, "Multiple Speakers found"
                        flag = 1
                        
                        source.set_name(Affiliation.text)
                        if DEBUG:
                            print (Affiliation.text)

                dialogue = Dialogue(source, '', '')
                for content in intervention.iter('Content'):
                    text = ""
                    for paratext in content.iter('ParaText'):
                        text += paratext.text

                    if DEBUG:
                        print("### Dialogue ###")
                        print(text)
                    
                    dialogue.set_conversation(text)

                # Add to the list of collections
                collection.add_dialogue(dialogue)
                list_of_collections.append(collection)
            
    return list_of_collections
    

collections = generate_dialogue_summary(text_data)

batch = []
batch_text = ""
word_count = 0
for collection in collections:
    for dialogue in collection.dialogues:
        batch_text += f"{dialogue.speaker.get_name()} said: {dialogue.conversation} \n"
        word_count += len(dialogue.speaker.get_name().split()) + len(dialogue.conversation.split())
        if word_count > 2500:
            batch.append(batch_text)
            batch_text = ""
            word_count = 0

if DEBUG:
    print(word_count)
    print(len(batch))

batch_summary = []
summary_size = 3000 / len(batch)

for text in batch:
    # Get the summary for each batch
    warnings.warn(f"Processing batch...{len(batch_summary) + 1}")
    response = ollama.chat(model='llama3', messages=[
                {
                    'role': 'user',
                    'content': f'Summarize this in less than {summary_size} words. Pick out only the most important points and mention the different views of parties in the discussion: {text}',
                },
            ])

    if DEBUG:
        print(text)
        print("\n")
        print(f"Summary ({len(response['message']['content'])} words):\n{response['message']['content']}")
        print("##############################################")

    batch_summary.append(response['message']['content'])

assert len(batch_summary) == len(batch), "Batch and batch_summary length mismatch"

# Summarize all the batch summaries
total_summary = "".join(batch_summary)
response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': f'Summarize the text below into a coherent article starting with the line "Today the parliament talked about". Use the markdown format: {total_summary}',
            },
        ])

print("\n\n")
print(response['message']['content'])

# Write summary to the file
# Get yesterday's date
yesterday = datetime.date.today() - datetime.timedelta(days = 1)

f = open(f"summary/debate-{yesterday}.md", "w")
f.write(response['message']['content'])
f.close()
