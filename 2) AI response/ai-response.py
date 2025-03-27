import google.generativeai as genai

genai.configure(api_key="")


model = genai.GenerativeModel("gemini-2.0-flash")


response = model.generate_content("What is Generative AI?")
print(response.text)
