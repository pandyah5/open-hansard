# For calling the API
import requests

# For calling the llama3 model
import ollama

# Read the XML content and parse it
from xml.etree import ElementTree as ET

# Import conversation.py
from conversation import Speaker, Dialogue, Collection

# For DEBUG
import warnings
DEBUG = 0

API_URL = 'https://www.ourcommons.ca/Content/House/441/Debates/314/HAN314-E.XML'
def call_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        text_data = response.text
        return text_data
    else:
        print("Failed to call the API.")

text_data = call_api(API_URL)

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
                # print("\n\n### New Intervention ###")
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
                    'content': f'Can you please summarize this text in less than {summary_size} words. Please pick out only the most important parts: {text}',
                },
            ])
    print(text)
    print("\n")
    print(f"Summary ({len(response['message']['content'])} words):\n{response['message']['content']}")
    batch_summary.append(response['message']['content'])
    print("##############################################")

assert len(batch_summary) == len(batch), "Batch and batch_summary length mismatch"

# Summarize all the batch summaries
total_summary = "".join(batch_summary)
response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': f'Can you please summarize the text below in a coherent manner: {total_summary}',
            },
        ])

print("\n\n")
print(response['message']['content'])
