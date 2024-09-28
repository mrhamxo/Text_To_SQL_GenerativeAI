import streamlit as st
import os 
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai

# load all the envirement variables
load_dotenv()

#configure Genai key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model
def get_gemini_response(question, prompt):
    
    model = genai.GenerativeModel("gemini-pro")
    
    response = model.generate_content([prompt[0], question])

    return response.text

# function to retrieve query from the database
def read_sql_query(sql, db):
    
    connect = sqlite3.connect(db)
    
    cursor = connect.cursor()
    cursor.execute(sql)
    
    rows = cursor.fetchall()
    
    connect.commit()
    connect.close()
    
    for row in rows:
        print(row)
    return rows    

# Define your Prompt
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

## Streamlit App
st.set_page_config(page_title = "I can retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key = "input")

submit = st.button("Ask the Question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is ")
    for row in response:
        print(row)
        st.header(row)