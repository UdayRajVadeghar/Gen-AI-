import tiktoken 

text = "Hello, world!"
encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode(text)

print("tokens : " , tokens)
print("Number of tokens:", len(tokens))
