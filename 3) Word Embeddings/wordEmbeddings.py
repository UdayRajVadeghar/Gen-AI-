import google.generativeai as genai
import numpy as np

genai.configure(api_key="")

text = "car"

response = genai.embed_content(
    model="models/embedding-001",  
    content=text,
    task_type="retrieval_document",  
)


embedding_vector = np.array(response["embedding"])


print("First 5 Values of Embedding Vector:", embedding_vector[:5])
print("Embedding Size:", embedding_vector.shape[0])  
