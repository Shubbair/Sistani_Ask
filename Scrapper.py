# ***-[ Hussain Salih Mahdi ]-***

# Get the content from the main website scrape it and save it as Q&A dataset
# TODO : 
# find tags , find route id , get the questions with answers

import requests
import json
from tqdm import tqdm
from bs4 import BeautifulSoup

URL = "https://www.sistani.org/arabic/qa/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="main-qa-content")

question_letters = results.find_all("a")

route = []

# get the tags and the routes for future enhance
for i in range(0,len(question_letters)):
    route.append(question_letters[i]['href'])
    tags.append(question_letters[i].string)

dataset = []

URL = "https://www.sistani.org"

# Loop over all the route and get page content
for i in tqdm(range(0,len(route))): 
    page = requests.get(URL+route[i])

    soup = BeautifulSoup(page.content, "html.parser")
    
    # Push all Q&A data into QAndA variable
    QAndA = soup.find_all("div", class_="one-qa")

    questions = 0
    answers = 0
    
    # Loop all QAndA data and separate questions , answers
    for spn in QAndA:
        # get the questions
        questions = spn.span.span.next_sibling
        # get the answers
        answers = spn.div.span.next_sibling

        dataset.append({
                questions.strip('\n') : answers.strip('\n')
        })

# Save data as JSON file
with open('Sistani_QA.json', 'w') as outfile:
    json.dump(dataset, outfile)
