import os
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from pymongo import MongoClient
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')  # Explicitly download `punkt_tab`


MONGO_HOST = "localhost"  # Docker container's host
MONGO_PORT = 27017  # Default MongoDB port
MONGO_DB = "text_chunks_db"  # Database name
MONGO_COLLECTION = "chunks"  # Collection name

# File to Process
TEXT_FILE = "c:/Users/gayat/GenAi/UpdatedAI/GenAi/rag/textfiles/text2.txt"

# Step 1: Load the text file
def load_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

# Step 2: Split text into sentences
def split_into_sentences(text):
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    return sentences

# Step 3: Generate sentence embeddings
def generate_embeddings(sentences):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(sentences)
    return embeddings

# Step 4: Cluster sentences based on semantic similarity
def cluster_sentences(sentences, embeddings, num_clusters=5):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(embeddings)

    clusters = {}
    for i, label in enumerate(kmeans.labels_):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(sentences[i])

    chunks = [" ".join(cluster) for cluster in clusters.values()]
    return chunks
connection_string = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"
# Step 5: Connect to MongoDB
def connect_to_mongo():
    # Include authSource in the connection string
    client = MongoClient(connection_string )
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    return collection

# Step 6: Save chunks to MongoDB
def save_chunks_to_mongo(chunks, collection):
    documents = [{"chunk": chunk} for chunk in chunks]
    collection.insert_many(documents)
    print(f"Saved {len(chunks)} chunks to MongoDB.")

# Step 7: Retrieve and Print First Two Lines of Each Chunk
def print_first_two_lines_from_db(collection):
    print("\nFirst two lines of each chunk from MongoDB:")
    for document in collection.find():
        chunk = document["chunk"]
        lines = chunk.split("\n")  # Split the chunk into lines
        first_two_lines = lines[:2]  # Get the first two lines
        print(" ".join(first_two_lines))  # Print the first two lines as a single string

# Main Process
def main():
    # Load and process the text
    text = load_text(TEXT_FILE)
    sentences = split_into_sentences(text)
    embeddings = generate_embeddings(sentences)

    # Cluster sentences into semantic chunks
    num_clusters = 5  # Adjust as needed
    chunks = cluster_sentences(sentences, embeddings, num_clusters=num_clusters)

    # Connect to MongoDB and save chunks
    collection = connect_to_mongo()
    save_chunks_to_mongo(chunks, collection)

    # Retrieve and print first two lines of each chunk
    print_first_two_lines_from_db(collection)

    print("\nSemantic chunking and MongoDB storage complete.")

if __name__ == "__main__":
    main()
