import pymongo
from sentence_transformers import SentenceTransformer

def store_text_in_mongo_with_embeddings(file_path, db_name, collection_name, embedding_model_name="all-MiniLM-L6-v2"):
    """
    Reads a text file, computes embeddings, and stores content with embeddings in MongoDB.

    Args:
        file_path (str): Path to the text file.
        db_name (str): Name of the MongoDB database.
        collection_name (str): Name of the MongoDB collection.
        embedding_model_name (str): Name of the SentenceTransformer model for embeddings.
    """
    # Initialize the SentenceTransformer model
    model = SentenceTransformer(embedding_model_name)

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    # Read the file and split into paragraphs
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    paragraphs = text.split("\n\n")  # Split into chunks by paragraph

    # Store each paragraph with embeddings as a document in MongoDB
    for idx, paragraph in enumerate(paragraphs):
        if paragraph.strip():  # Ignore empty paragraphs
            embedding = model.encode(paragraph.strip()).tolist()  # Compute embedding
            collection.insert_one({
                "chunk_id": idx,
                "text": paragraph.strip(),
                "embedding": embedding  # Add embedding to the document
            })

    print(f"Text from {file_path} has been stored in MongoDB with embeddings.")

# Example usage
if __name__ == "__main__":
    store_text_in_mongo_with_embeddings("scraped_content.txt", "web_scraper", "scraped")
