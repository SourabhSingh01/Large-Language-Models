import sqlite3

## connect to Sqlite
connection = sqlite3.connect("student.db")

## create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''Insert Into STUDENT values('Sourabh', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Shivali', 'SAP', 'A', 94)''')
cursor.execute('''Insert Into STUDENT values('Suchender', 'SAP', 'B', 78)''')
cursor.execute('''Insert Into STUDENT values('Jigar', 'AI', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Meenal', 'Computer Science', 'A', 90)''')

## Display all the records
print ("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close