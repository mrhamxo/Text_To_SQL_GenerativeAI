import streamlit as st
import os 
import sqlite3 
from dotenv import load_dotenv 
import google.generativeai as genai

# Load all the environment variables
load_dotenv()

# Configure Google Generative AI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the Gemini model based on a question and a predefined prompt
def get_gemini_response(question, prompt):
    
    model = genai.GenerativeModel("gemini-pro")  # Load the "gemini-pro" model from the Google Generative AI

    # Use the model to generate content based on the prompt and the question
    response = model.generate_content([prompt[0], question])

    return response.text  # Return the text of the generated response

# Function to execute a SQL query on a SQLite database and return the results
def read_sql_query(sql, db):
    
    connect = sqlite3.connect(db)  # Establish a connection to the SQLite database specified by `db`
    
    cursor = connect.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute(sql)  # Execute the SQL query provided in the `sql` variable
    
    rows = cursor.fetchall()  # Fetch all the rows returned by the SQL query
    
    connect.commit()  # Commit any changes to the database (not necessary for SELECT queries but a good practice)
    connect.close()  # Close the connection to the database
    
    for row in rows:  # Iterate over each row in the result set
        print(row)  # Print each row for debugging purposes
    return rows

# Define your Prompt for converting English questions into SQL queries
prompt = [
    """
    You are an expert in converting English questions to SQL query! 
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example, \nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; 
    \nExample 2 - Tell me all the students studying in Data Science class ?, 
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS = "Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit App Interface
st.set_page_config(page_title="I can retrieve Any SQL query")  # Set the page title for the Streamlit app
st.header("Gemini App To Retrieve SQL Data")  # Display the header text on the web page

question = st.text_input("Input: ", key="input")  # Input box where users can enter their natural language questions

submit = st.button("Ask the Question")  # Button that the user clicks to submit the question

# If the submit button is clicked
if submit:
    response = get_gemini_response(question, prompt)  # Get the SQL query by passing the user's question and the prompt to the Gemini model
    print(response)  # Print the generated SQL query for debugging purposes
    
    response = read_sql_query(response, "student.db")  # Execute the generated SQL query on the "student.db" database
    
    st.subheader("The Response is ")  # Display a subheader for the result
    for row in response:  # Iterate through the rows returned by the SQL query
        print(row)  # Print each row for debugging purposes
        st.header(row)  # Display each row on the web page using Streamlit's header function
