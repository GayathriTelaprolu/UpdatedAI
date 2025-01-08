import requests
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util

# MongoDB Configuration
MONGO_USERNAME = "admin"
MONGO_PASSWORD = "password"
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "text_chunks_db"
MONGO_COLLECTION = "chunks"

# Groq API Configuration
GROQ_API_KEY = "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"  # Replace with your actual Groq API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Load SentenceTransformer for retrieval
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Step 1: Connect to MongoDB
def connect_to_mongo():
    client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/")
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    return collection


# Step 2: Retrieve Relevant Chunks
def retrieve_relevant_chunks(query, collection, top_k=3):
    # Retrieve all chunks from MongoDB
    chunks = [doc["chunk"] for doc in collection.find()]

    # Compute embeddings for query and chunks
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    chunk_embeddings = embedding_model.encode(chunks, convert_to_tensor=True)

    # Calculate similarity scores
    scores = util.pytorch_cos_sim(query_embedding, chunk_embeddings)[0]

    # Rank chunks by similarity
    top_results = scores.topk(top_k)
    relevant_chunks = [(chunks[idx], scores[idx].item()) for idx in top_results.indices]

    return relevant_chunks


# Step 3: Generate Answer with Groq API
def generate_answer_with_groq(query, context):
    payload = {
        "model": "llama-3.3-70b-versatile",  # Replace with the specific model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Question: {query}\nContext: {context}"}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API error: {response.status_code} - {response.text}")


# Step 4: Process Answer with Groq API Agent
def process_answer_with_agent_groq(answer):
    """
    Processes the answer by using Groq's API to convert it into a meaningful paragraph if needed.
    """
    # Check if the answer contains bullet points or a list
    if "\n" in answer or any(char in answer for char in ["-", "*", "1.", "2.", "3."]):
        print("\nThe answer seems to be in bullet points or list format. Reformatting using Groq API...")

        payload = {
            "model": "llama-3.3-70b-versatile",  # Replace with the specific model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant who reformats text."},
                {"role": "user", "content": f"Convert the following points into a meaningful paragraph:\n{answer}"}
            ],
            "temperature": 0.7,
            "max_tokens": 300
        }
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Groq API error: {response.status_code} - {response.text}")
    else:
        # If the answer is already a paragraph
        return "The answer is already in paragraph format. No conversion needed."


# Main Function
def main():
    # Connect to MongoDB
    collection = connect_to_mongo()

    # Get user query
    query = input("Enter your query: ")

    # Retrieve relevant chunks
    print("\nRetrieving relevant chunks...")
    relevant_chunks = retrieve_relevant_chunks(query, collection, top_k=3)
    for idx, (chunk, score) in enumerate(relevant_chunks, 1):
        print(f"Chunk {idx}: {chunk[:100]}... (Score: {score:.4f})")

    # Combine relevant chunks into a context
    context = " ".join([chunk for chunk, _ in relevant_chunks])

    # Generate answer using Groq API
    print("\nGenerating answer...")
    try:
        answer = generate_answer_with_groq(query, context)
        print("\nGenerated Answer:")
        print(answer)

        # Process the answer with the agent
        print("\nProcessing answer with agent...")
        final_output = process_answer_with_agent_groq(answer)
        print("\nAgent Output:")
        print(final_output)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
