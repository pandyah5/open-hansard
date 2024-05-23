# For calling the API
import requests

# Read the XML content and parse it
from xml.etree import ElementTree as ET

def call_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        text_data = response.text
        return text_data
    else:
        print("Failed to call the API.")

# Replace 'API_URL' with the actual URL of the API you want to call
# API_URL = 'https://api.openparliament.ca/politicians/?format=json'
API_URL = 'https://www.ourcommons.ca/Content/House/441/Debates/314/HAN314-E.XML'
text_data = call_api(API_URL)

# Find the first occurence of <?xml version="1.0" encoding="UTF-8"?> in text_data and remove everything before it
xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
text_data = text_data[text_data.find(xml_declaration):]

# For each SubjectOfBusiness element within HansardBody, print the PersonSpeaking
def parse_xml(xml_content):
    root = ET.fromstring(xml_content).find('HansardBody')
    for subject_of_business in root.iter('SubjectOfBusiness'):
        for content in subject_of_business.iter('SubjectOfBusinessContent'):
            for intervention in content.iter('Intervention'):
                for speaker in intervention.iter('PersonSpeaking'):
                    for Affiliation in speaker.iter('Affiliation'):
                        print (Affiliation.text)

                for content in intervention.iter('Content'):
                    for paratext in content.iter('ParaText'):
                        print (paratext.text)

                print("--------------------------------------------------")

parse_xml(text_data)