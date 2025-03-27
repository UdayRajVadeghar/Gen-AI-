# Tokenization :

## What is tokenization:

Tokenization is the process of breaking text into smaller pieces (tokens) so that AI models can understand and process it.

**Example**:
Text: "Hello, world!" <br>
Tokens: ["Hello", ",", " world", "!"]<br>
Tokens: [9906, 11, 1917, 0]<br>
length: 4 tokens<br>

AI doesn't read words like humans—it converts them into tokens and numbers to analyze and generate responses.

# Word Embeddings

## What is Word Embeddings?

Word embeddings are numerical representations of words in a high-dimensional vector space (usually 768 dimentions or sometimes 1536 dimentions), where words with similar meanings have closer embeddings.

**Example**
for dog: the word embedding of the first my elements of the 768 elements are <br>
First 5 Values of Embedding Vector: [ 0.04773374 -0.01116747 -0.07980476 -0.00795903 0.03336207] <br>

for animal : the word embedding of the first my elements of the 768 elements are <br>
First 5 Values of Embedding Vector: [ 0.03497596 -0.01609279 -0.07792687 -0.00145578 0.04086112] <br>

for car : the word embedding of the first my elements of the 768 elements are <br>
First 5 Values of Embedding Vector: [ 0.02331771 -0.02176642 -0.08740393 -0.02260794 0.0398842 ] <br>

## -> As we can see that the embedding vectors of the dog and animal are close whereas the vector embedding of the car is totally different and far way. This is how AI establishes the similarity/relationships between the words.
