# For calling the API
import requests

# For calling the llama3 model
import ollama

# Read the XML content and parse it
from xml.etree import ElementTree as ET

# Import conversation.py
from conversation import Speaker, Dialogue, Collection

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
                print("\n\n### New Intervention ###")
                collection = Collection('')
                source = Speaker('', '')
                for speaker in intervention.iter('PersonSpeaking'):
                    flag = 0
                    # print("### Speaker ###")
                    for Affiliation in speaker.iter('Affiliation'):
                        if flag == 1:
                            assert False, "Multiple Speakers found"
                        flag = 1
                        
                        source.set_name(Affiliation.text)
                        # print (Affiliation.text)

                dialogue = Dialogue(source, '', '')
                for content in intervention.iter('Content'):
                    text = ""
                    for paratext in content.iter('ParaText'):
                        text += paratext.text
                    # print("### Dialogue ###")
                    # print(text)
                    dialogue.set_conversation(text)

                # Add to the list of collections
                collection.add_dialogue(dialogue)
                list_of_collections.append(collection)

            # Get summary for the intervention

            # response = ollama.chat(model='llama3', messages=[
            #     {
            #         'role': 'user',
            #         'content': f'Can you please summarize the text and pick out the important parts: {dialogue.get_conversation()}',
            #     },
            # ])

            # Update word_counter
            # word_counter += len(source.get_name().split()) + len(dialogue.get_conversation().split())
            
    return list_of_collections
    

collections = generate_dialogue_summary(text_data)

word_count = 0
for collection in collections:
    # print(intervention.title)
    for dialogue in collection.dialogues:
        # print(dialogue.speaker.get_name())
        # print(dialogue.conversation)
        # print(dialogue.conversation_summary)
        word_count += len(dialogue.speaker.get_name().split()) + len(dialogue.conversation.split())

print(word_count)
