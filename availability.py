import re
import math
import requests
from bs4 import BeautifulSoup

def get_parliament_and_session_id():
    # URL of the webpage to scrape
    url = "https://www.ourcommons.ca/en/parliamentary-business/"

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all elements with the session-subtitle class
        session_subtitles = soup.find_all(class_="session-subtitle")

        # Print the text content of each session-subtitle element
        for subtitle in session_subtitles:
            # regex object 
            sessionNumRegex = re.compile(r'(\d{1,2})(?:st|nd|rd|th) Session') 
            parliamentNumRegex = re.compile(r'(\d{1,2})(?:st|nd|rd|th) Parliament')

            session_num = sessionNumRegex.search(subtitle.text).group(1)
            parliament_num = parliamentNumRegex.search(subtitle.text).group(1)

            return parliament_num, session_num
    else:
        print("Failed to retrieve the webpage")
        return None, None

def is_debate_available(parliament_num, session_num, debate_num):
    API_URL = f'https://www.ourcommons.ca/Content/House/{parliament_num}{session_num}/Debates/{debate_num}/HAN{debate_num}-E.XML'
    response = requests.get(API_URL)
    if response.status_code == 200:
        return True
    else:
        return False

def get_new_debate(parliament_num, session_num):
    # Read the last retrieved data
    with open("last-retrieved.txt", "r") as file:
        last_retrieved_data = file.read().split('-')
        file.close()

    print("Last retrieved data: ", last_retrieved_data)

    # Check if the last retrieved data matches the current data
    if last_retrieved_data[0] == parliament_num and last_retrieved_data[1] == session_num:
        print("Parliament and Session number have not changed since the last retrieval")
        
        # Check if the next debate number is available
        last_debate_number = int(last_retrieved_data[2])
        last_retrieved_data[2] = "0"*(2 - int(math.log(last_debate_number + 1, 10))) + str(last_debate_number + 1)
        print(last_retrieved_data[2])
        if is_debate_available(last_retrieved_data[0], last_retrieved_data[1], last_retrieved_data[2]):
            # Update the debate number
            with open("last-retrieved.txt", "w") as file:
                file.write('-'.join(last_retrieved_data))
                file.close()

            print("New debate found here: ", f"https://www.ourcommons.ca/Content/House/{last_retrieved_data[0]}{last_retrieved_data[1]}/Debates/{last_retrieved_data[2]}/HAN{last_retrieved_data[2]}-E.XML")
            with open("new-debate.txt", "w") as file:
                file.write(f"https://www.ourcommons.ca/Content/House/{last_retrieved_data[0]}{last_retrieved_data[1]}/Debates/{last_retrieved_data[2]}/HAN{last_retrieved_data[2]}-E.XML")
                file.close()
            return True

    elif last_retrieved_data[0] == parliament_num and last_retrieved_data[1] != session_num:
        print("Session number has been updated since the last retrieval")

        # Update the session and reset the debate number
        last_retrieved_data[1] = str(int(last_retrieved_data[1]) + 1)
        last_retrieved_data[2] = "001"

        if is_debate_available(last_retrieved_data[0], last_retrieved_data[1], last_retrieved_data[2]):
            # Update the debate number
            with open("last-retrieved.txt", "w") as file:
                file.write('-'.join(last_retrieved_data))
                file.close()

            print("New debate found here: ", f"https://www.ourcommons.ca/Content/House/{last_retrieved_data[0]}{last_retrieved_data[1]}/Debates/{last_retrieved_data[2]}/HAN{last_retrieved_data[2]}-E.XML")
            with open("new-debate.txt", "w") as file:
                file.write(f"https://www.ourcommons.ca/Content/House/{last_retrieved_data[0]}{last_retrieved_data[1]}/Debates/{last_retrieved_data[2]}/HAN{last_retrieved_data[2]}-E.XML")
                file.close()
            return True

    else:
        print("Parliament number has been updated since the last retrieval")

        # Update the parliament and reset session and debate number
        last_retrieved_data[0] = str(int(last_retrieved_data[0]) + 1)
        last_retrieved_data[1] = "1"
        last_retrieved_data[2] = "001"

        if is_debate_available(last_retrieved_data[0], last_retrieved_data[1], last_retrieved_data[2]):
            with open("last-retrieved.txt", "w") as file:
                file.write('-'.join(last_retrieved_data))
                file.close()

            print("New debate found here: ", f"https://www.ourcommons.ca/Content/House/{last_retrieved_data[0]}{last_retrieved_data[1]}/Debates/{last_retrieved_data[2]}/HAN{last_retrieved_data[2]}-E.XML")
            with open("new-debate.txt", "w") as file:
                file.write(f"https://www.ourcommons.ca/Content/House/{last_retrieved_data[0]}{last_retrieved_data[1]}/Debates/{last_retrieved_data[2]}/HAN{last_retrieved_data[2]}-E.XML")
                file.close()

            return True

    print("No new debate available")
    return False

    