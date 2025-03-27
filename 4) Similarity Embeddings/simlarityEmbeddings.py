import google.generativeai as genai
import numpy as np


genai.configure(api_key="")

def get_embedding(text):
    response = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document",
    )
    return np.array(response["embedding"])

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

text1 = "dont do drugs"
text2 = "drugs are bad"

embedding1 = get_embedding(text1)
embedding2 = get_embedding(text2)

similarity = cosine_similarity(embedding1, embedding2)

print(f"Similarity Score: {similarity:.4f}")  
