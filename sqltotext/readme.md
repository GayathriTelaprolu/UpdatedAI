# SQL Query Generator and Executor

This project automates the conversion of natural language queries into SQL queries, executes them against a MySQL database, and translates the results back into natural language using OpenAI's GPT models. It is designed to simplify database interactions for users who may not be familiar with SQL syntax.

## Features

- **Natural Language to SQL**: Converts user-inputted natural language queries into executable SQL commands.
- **Execute SQL Queries**: Runs the generated SQL queries against a predefined MySQL database.
- **Natural Language Summaries**: Utilizes OpenAI's GPT models to provide summaries of the SQL query results in natural language.
- **Streamlit Interface**: Provides a simple and interactive web interface for users to input queries and view results.

## Prerequisites

- Python 3.8 or higher
- MySQL Server
- OpenAI API key

## Setup

### Dependencies

Install the required Python libraries:

```bash
pip install streamlit mysql-connector-python python-dotenv openai



get_sql_query.py: Handles the conversion of natural language queries into SQL.
execute_sql_query.py: Executes the SQL queries on the MySQL database and translates results.
main.py: The main Streamlit application script for the web interface.