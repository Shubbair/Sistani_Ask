import os
import json
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get('API_KEY'))

qa_data = open('Sistani_QA.json')
qa_data = json.load(qa_data)

data_frame = pd.DataFrame(qa_data)
data_frame.head()