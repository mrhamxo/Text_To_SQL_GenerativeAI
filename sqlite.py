import sqlite3

## connect to SQLite
connection = sqlite3.connect("student.db")  # Create or connect to a database file named 'student.db'

#create a cursor object to insert record, create table
cursor = connection.cursor()  # Create a cursor object, which allows you to execute SQL commands

# create the table
table_info = """
CREATE table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
# Define an SQL command to create a table named STUDENT with columns NAME, CLASS, SECTION, and MARKS

cursor.execute(table_info)  # Execute the SQL command to create the STUDENT table

# insert some more records
cursor.execute('''insert into STUDENT values('Hamza', 'Data Science', 'A', 100)''')  
cursor.execute('''insert into STUDENT values('Shakir', 'Machincal Engineering', 'B', 90)''')  
cursor.execute('''insert into STUDENT values('Safdar', 'Electrical Engineering', 'C', 80)''')  
cursor.execute('''insert into STUDENT values('Umar', 'Computer Science', 'A', 70)''')  
cursor.execute('''insert into STUDENT values('Danyal', 'Civil Engineering', 'B', 60)''')  

# Display all the table
print("The Inserted records are")  # Print a message to indicate the records that will be displayed

data = cursor.execute('''select * from STUDENT''')  # Execute an SQL query to select all records from the STUDENT table

for row in data:  # Loop through each record returned by the query
    print(row)  # Print each row (record) to the console

# commit your change into the database
connection.commit()  # Commit the changes to the database to make sure all the inserted data is saved

connection.close()  # Close the connection to the database
