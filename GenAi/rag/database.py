from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np

# Function to read the content of a text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to chunk text into smaller pieces (sentences or fixed-size chunks)
def chunk_text(text, chunk_size=50):
    # Split the text into sentences (or you can split by paragraphs if needed)
    sentences = text.split('. ')  # Basic sentence splitting (can be refined)
    
    # Further chunk sentences into fixed-size chunks if needed
    chunks = [sentences[i:i + chunk_size] for i in range(0, len(sentences), chunk_size)]
    return [' '.join(chunk) for chunk in chunks]  # Join sentences back to form a chunk

# Load the pre-trained SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Read content from a text file
file_path = 'C:/Users/Public/genai1/GenAi/rag/textfiles/text1.txt'  # Replace with the path to your text file
text_content = read_text_file(file_path)

# Chunk the text into smaller units (sentences, paragraphs, etc.)
chunks = chunk_text(text_content, chunk_size=5)  # Adjust chunk_size as needed

# Generate embeddings for each chunk
embeddings = model.encode(chunks, convert_to_tensor=True)

# Convert embeddings to NumPy array for storage
embeddings = embeddings.cpu().detach().numpy()

# Initialize Chroma client and collection
client = chromadb.Client()
collection = client.create_collection(name="text_chunks_collection")

# Generate unique IDs for each chunk (could be index or custom string)
ids = [f"chunk_{i}" for i in range(len(chunks))]

# Store embeddings and their corresponding chunks in Chroma
for i, chunk in enumerate(chunks):
    collection.add(
        ids=[ids[i]],          # Unique ID for each chunk
        documents=[chunk],     # Document (text) for this chunk
        metadatas=[{"index": i}],  # Metadata associated with each chunk (optional)
        embeddings=[embeddings[i]]   # The embedding for each chunk
    )

# Perform similarity search
query = "Why choose the US for study? Why not the UK, Canada or Australia?"
query_embedding = model.encode([query], convert_to_tensor=True)
query_embedding = query_embedding.cpu().detach().numpy()

# Perform the search in Chroma (find the most similar chunk)
results = collection.query(
    query_embeddings=query_embedding.tolist(),  # Convert query embedding to list
    n_results=2  # Number of results to retrieve
)

# Print the results
print("Query: ", query)
for result in results['documents']:
    print("Similar Chunk: ", result)
