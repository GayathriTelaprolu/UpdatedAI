from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np

# Load the pre-trained SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example: Let's assume `chunks` is a list of text chunks
chunks = [
    "Natural language processing (NLP) is a field of artificial intelligence concerned with the interactions between computers and human languages.",
    "Challenges in natural language processing involve natural language understanding, generation, and machine perception."
]

# Generate embeddings for each chunk
embeddings = model.encode(chunks, convert_to_tensor=True)

# Convert embeddings to NumPy array for storage
embeddings = embeddings.cpu().detach().numpy()
print(embeddings)
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
query = "What is natural language processing?"
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
