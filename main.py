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

for idx in range(len(qa_data)):
    questions.append(list(qa_data[idx].keys()))

# to remove inside list
questions = np.array(questions).flatten()

# to remove special character
cleaned_questions = [re.sub('[^?-?]', ' ', question) for question in questions]
cleaned_questions = [re.sub('[؟:]', ' ', question) for question in questions]

# make dataframe and append the question
data_frame = pd.DataFrame(cleaned_questions)
data_frame.columns = ['question']

model = 'models/embedding-001'
def embed_fn(text):
  return genai.embed_content(model=model,
                             content=text,
                             task_type="retrieval_document",
                            )["embedding"]

data_frame['Embeddings'] = data_frame.apply(lambda row: embed_fn(row['question']), axis=1)
print(data_frame.head())
