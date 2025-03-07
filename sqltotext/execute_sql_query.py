import mysql.connector
from mysql.connector import Error
import openai
import os
from dotenv import load_dotenv
load_dotenv()


# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def execute_sql_query(sql_query):
    """ Execute SQL query and return results """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='call_data',
            user='root',
            password='Gayathri@123'
        )
        cursor = connection.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def translate_results_to_natural_language(results,natural_language_query):
    """ Convert query results to natural language using OpenAI's LLM """
    #prompt=f"Translate these SQL results into a natural language summary: {results_str}",
    try:
        results_for_prompt=results
        query=natural_language_query
        #prompt=f"Translate these SQL results into a natural language summary: {results}", # Simplifying results to a string
        response = openai.chat.completions.create(
        model="gpt-4",  # or another suitable model
        messages=[
            {"role": "system", "content":  "You are an assistant that analyzes data."},
            {"role": "user", "content":f"explain sql query results in natural language for the query {query} and results are {results_for_prompt}"}
        ],
        max_tokens=250
    )
    
     # Adjusted for correct attribute access
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in translating results: {e}")
        return None


