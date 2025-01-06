import os
from sentence_transformers import SentenceTransformer
import chromadb

# Function to read the content of the text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to check for new content (compare with previous text)
def get_new_text(file_path, last_processed_text):
    current_text = read_text_file(file_path)
    if current_text == last_processed_text:
        return "", current_text  # No new content
    # New content is the difference between the current and last processed text
    new_text = current_text[len(last_processed_text):]
    return new_text, current_text

# Function to process new text and add to Chroma DB
def process_new_text(new_text, client, collection, last_processed_text):
    if not new_text:
        print("No new text to process.")
        return last_processed_text

    # Load pre-trained SBERT model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Split the new text into chunks (sentences or fixed-size chunks)
    chunks = new_text.split('. ')  # Basic sentence splitting, adjust as needed

    # Generate embeddings for each new chunk
    embeddings = model.encode(chunks, convert_to_tensor=True)
    embeddings = embeddings.cpu().detach().numpy()

    # Generate unique IDs for each chunk (could be index or custom string)
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Store embeddings and their corresponding chunks in Chroma DB
    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[ids[i]],          # Unique ID for each chunk
            documents=[chunk],     # Document (text) for this chunk
            embeddings=[embeddings[i]]   # The embedding for each chunk
        )

    return last_processed_text

# Function to track the last processed text
def get_last_processed_text():
    # Check if we have a saved position file
    if os.path.exists("last_processed_text.txt"):
        with open("last_processed_text.txt", 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = ""  # Start fresh if no file exists
    return text

# Function to update the last processed text
def update_last_processed_text(text):
    with open("last_processed_text.txt", 'w', encoding='utf-8') as file:
        file.write(text)
def query_chroma(query, model, collection):
    # Encode the query into an embedding using the pre-trained SBERT model
    query_embedding = model.encode([query], convert_to_tensor=True)
    query_embedding = query_embedding.cpu().detach().numpy()

    # Perform the search in Chroma DB (find the most similar chunk)
    results = collection.query(
        query_embeddings=query_embedding.tolist(),  # Convert query embedding to list
        n_results=2  # Number of results to retrieve
    )

    # Print the results of the query
    print(f"Query: {query}")
    print("Top Similar Chunks:")
    for result in results['documents']:
        print(f"- {result}")


# Main process
file_path = 'C:/Users/Public/genai1/GenAi/rag/textfiles/text1.txt' 
client = chromadb.Client()
collection = client.create_collection(name="text_chunks_collection")

# Get the last processed text from file (empty if this is the first run)
last_processed_text = get_last_processed_text()

# Get new text from the file by comparing with last processed text
new_text, updated_text = get_new_text(file_path, last_processed_text)

# Process the new text if available
last_processed_text = process_new_text(new_text, client, collection, last_processed_text)

# Update the last processed text after processing the new text
update_last_processed_text(updated_text)

# Print the newly added text
if new_text:
    print("New Text Added:")
    print(new_text)
else:
    print("No new text added.")


query = "What is natural language processing?"
query_chroma(query, SentenceTransformer('paraphrase-MiniLM-L6-v2'), collection)