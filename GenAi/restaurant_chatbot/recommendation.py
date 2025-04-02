import os
import requests
from pymongo import MongoClient, errors
from sentence_transformers import SentenceTransformer
import numpy as np
from langchain_core.tools import Tool
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment Variables
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 1: Fetch Weather Data
def get_weather(city):
    """
    Fetch the current weather for a given city.
    """
    if not WEATHER_API_KEY:
        return "unknown"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=10).json()
        if response.get("main"):
            temperature = response["main"]["temp"]
            return "cold" if temperature < 15 else "warm"
        else:
            return "unknown"
    except requests.exceptions.RequestException as e:
        print(f"Weather API Error: {e}")
        return "unknown"

# Step 2: Connect to MongoDB
def connect_to_mongo(db_name="web_scraper", collection_name="scraped"):
    """
    Connect to MongoDB and return the collection.
    """
    try:
        client = MongoClient(MONGO_URI)
        db = client[db_name]
        return db[collection_name]
    except errors.ConnectionFailure as e:
        print(f"MongoDB Connection Error: {e}")
        return None

# Step 3: Perform Semantic Search
def semantic_search(user_query, collection, embedding_model_name="all-MiniLM-L6-v2", top_k=5):
    """
    Perform semantic search on MongoDB data.

    Args:
        user_query (str): The user's query.
        collection (pymongo.collection.Collection): The MongoDB collection.
        embedding_model_name (str): SentenceTransformer model name.
        top_k (int): Number of top results to return.

    Returns:
        List[Dict]: Top-k matching documents.
    """
    try:
        model = SentenceTransformer(embedding_model_name)
        query_embedding = model.encode(user_query)

        results = []
        for doc in collection.find():
            doc_embedding = np.array(doc.get("embedding", []))
            if len(doc_embedding) > 0:
                similarity = np.dot(query_embedding, doc_embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
                )
                # Filter only relevant content (e.g., exclude noisy/irrelevant text)
                if similarity > 0.5:  # Filter for high similarity
                    results.append((similarity, doc))

        # Sort by similarity and return top_k results
        results = sorted(results, key=lambda x: x[0], reverse=True)[:top_k]
        return [
            {
                "text": doc["text"][:500] + "..." if len(doc["text"]) > 500 else doc["text"],  # Truncate long text
                "similarity": round(score, 2)
            }
            for score, doc in results
        ]
    except Exception as e:
        print(f"Semantic Search Error: {e}")
        return []


# Step 4: Recommendation Logic
def recommend_items(user_query, weather, collection):
    """
    Recommend items based on user query and weather.
    """
    if collection is None:
        return "Sorry, the database is not available."

    matching_items = semantic_search(user_query, collection)

    if not matching_items:
        return "Sorry, we couldn't find anything matching your query."

    if weather == "cold" and "cold" in user_query.lower():
        return "The weather is cold. Would you prefer something warm instead? Here are some suggestions:\n" + \
               "\n".join([f"- {doc['text']}" for doc in semantic_search("warm", collection)])
    elif weather == "warm" and "hot" in user_query.lower():
        return "The weather is warm. Would you prefer something cold instead? Here are some suggestions:\n" + \
               "\n".join([f"- {doc['text']}" for doc in semantic_search("cold", collection)])
    else:
        return "Here are the matching items based on your query:\n" + \
               "\n".join([f"- {doc['text']}" for doc in matching_items])

# Step 5: Weather-Based Recommendation Tool
def recommendation_tool(user_query, city):
    """
    Weather-based recommendation tool that fetches weather and provides recommendations.
    """
    # Connect to MongoDB
    collection = connect_to_mongo()

    if collection is None:
        return "Database connection failed. Please try again later."

    # Get current weather
    weather = get_weather(city)

    # Generate recommendations
    return recommend_items(user_query, weather, collection)

# Update LangChain agent definition
def create_agent():
    """
    Create a LangChain agent with tools for weather and recommendations.
    """
    tools = [
        Tool(
            name="WeatherTool",
            func=lambda city: get_weather(city),
            description="Fetch the current weather for a given city."
        ),
        Tool(
            name="RecommendationTool",
            func=lambda query_city: recommendation_tool(*query_city),
            description="Provide item recommendations based on user query and weather."
        )
    ]

    llm = OpenAI(api_key=OPENAI_API_KEY)
    return tools, llm

# Example Usage
if __name__ == "__main__":
    tools, llm = create_agent()
    city = "New York"
    user_query = "hot coffee"

    try:
        recommendation = recommendation_tool(user_query, city)
        print(recommendation)
    except Exception as e:
        print(f"Error: {e}")
