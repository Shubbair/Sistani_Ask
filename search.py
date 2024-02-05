import os
import numpy as np
import pandas as pd
import google.generativeai as genai

genai.configure(api_key=os.environ.get('API_KEY'))
model = 'models/embedding-001'

query = "How do you shift gears in the Google car?"
model = 'models/embedding-001'

request = genai.embed_content(model=model,
                              content=query,
                              task_type="retrieval_query")
print(request)

# def find_best_passage(query, dataframe):
#   """
#   Compute the distances between the query and each document in the dataframe
#   using the dot product.
#   """
#   query_embedding = genai.embed_content(model=model,
#                                         content=query,
#                                         task_type="retrieval_query")["embedding"]
#   dot_products = np.dot(np.stack(dataframe['embeddings']), query_embedding)
#   idx = np.argmax(dot_products)
#   return dataframe.iloc[idx]

# dataset = pd.read_csv('istifta.csv')

# print(find_best_passage('ما هو حكم الدم على الملابس؟ ',dataset))
