import streamlit as st
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util
from query_answering import retrieve_relevant_chunks, generate_answer_with_groq, process_answer_with_agent_groq

# MongoDB Configuration
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "web_scraper"
MONGO_COLLECTION = "scraped"

# Function to connect to MongoDB
def connect_to_mongo():
    client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    return collection

# Streamlit Interface
st.title("Gayathri's chatbot")
st.write("Ask your questions about the Indian stock market.")

# User Input
user_query = st.text_input("Enter your query:")

# Chatbot Response
if st.button("Ask"):
    if user_query.strip():
        try:
            # Connect to MongoDB
            collection = connect_to_mongo()

            # Retrieve relevant chunks
            relevant_chunks = retrieve_relevant_chunks(user_query, collection, top_k=3)
            context = " ".join([chunk for chunk, _ in relevant_chunks])

            # Generate response
            answer = generate_answer_with_groq(user_query, context)
            st.write(f"**Chatbot Response:** {answer}")

            # Process answer with Groq agent
            processed_answer = process_answer_with_agent_groq(answer)
            st.write(f"**Processed Answer:** {processed_answer}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query before clicking 'Ask'.")
