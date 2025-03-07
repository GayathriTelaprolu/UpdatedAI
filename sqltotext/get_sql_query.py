import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
def get_sql_query(natural_language_query, schema_prompt):
    """ Convert natural language query to SQL using OpenAI's Codex with schema context. """
    try:
        full_prompt = f"{schema_prompt}\nTranslate this natural language query into an SQL query: {natural_language_query}\n\n###\n\n"
        response = openai.chat.completions.create(
        model="gpt-4",  # or another suitable model
        messages=[
            {"role": "system", "content":  "You are an assistant that analyzes data."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=250
    )
    
     # Adjusted for correct attribute access
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in generating SQL query: {e}")
        return None


