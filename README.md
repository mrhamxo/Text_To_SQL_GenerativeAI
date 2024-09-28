# Text_To_SQL_GenerativeAI App

This project demonstrates how to convert natural language questions into SQL queries using Google's Gemini model and retrieve the results from a SQLite database. The application uses Streamlit as the user interface, making it simple to input questions and retrieve corresponding data from the database.

## Project Overview

The app allows users to enter questions in English, and the underlying Gemini model translates them into SQL queries. These queries are then executed on a SQLite database (`student.db`) to fetch and display the relevant results.

### Features

- **Natural Language to SQL**: Converts English questions into SQL queries.
- **Google Gemini Integration**: Uses the Gemini model for language processing.
- **SQLite Database**: Queries are run on a local `student.db` database.
- **Streamlit Interface**: Provides an easy-to-use interface for inputting questions and viewing results.
