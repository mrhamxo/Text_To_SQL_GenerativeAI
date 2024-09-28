import sqlite3

## connect to SQLite
connection = sqlite3.connect("student.db")

#create a cursor object to insert record, create table
cursor = connection.cursor()

# create the table
table_info = """
CREATE table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

# insert some more records
cursor.execute('''insert into STUDENT values('Hamza', 'Data Science', 'A', 100)''')
cursor.execute('''insert into STUDENT values('Shakir', 'Machincal Engineering', 'B', 90)''')
cursor.execute('''insert into STUDENT values('Safdar', 'Electrical Engineering', 'C', 80)''')
cursor.execute('''insert into STUDENT values('Umar', 'Computer Science', 'A', 70)''')
cursor.execute('''insert into STUDENT values('Danyal', 'Civil Engineering', 'B', 60)''')

# Display all the table 
print("The Inserted records are")
data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

# commit your change into the database
connection.commit()
connection.close()