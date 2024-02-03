import os
import re
import json
import numpy as np
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get('API_KEY'))

qa_data = open('Sistani_QA.json')
qa_data = json.load(qa_data)

questions = []
answers = []

for idx in range(len(qa_data)):
    questions.append(list(qa_data[idx].keys()))
    answers.append(list(qa_data[idx].values()))

# to remove inside list
questions = np.array(questions).flatten()
answers = np.array(answers).flatten()

# to remove special character
cleaned_questions = [re.sub('[^?-?]', ' ', question) for question in questions]
cleaned_questions = [re.sub('[؟:]', ' ', question) for question in questions]

cleaned_answers = [re.sub('[؟:]', ' ', answer) for answer in answers]

# make dataframe and append the question
data_frame = pd.DataFrame({'question':cleaned_questions,'answer':cleaned_answers})

data_frame = data_frame[:10]

model = 'models/embedding-001'
def embed_fn(title, text):
  return genai.embed_content(model=model,
                             content=text,
                             task_type="retrieval_document",
                             title=title)["embedding"]

data_frame['embeddings'] = data_frame.apply(lambda row: embed_fn(row['question'],row['answer']), axis=1)
print(data_frame.head())
