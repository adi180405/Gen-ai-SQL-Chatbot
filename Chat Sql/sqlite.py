import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to insert record,create table
cursor=connection.cursor()

## create table
'''table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""'''
#cursor.execute(table_info)

#insert some more records
cursor.execute(''' INSERT INTO STUDENT VALUES('KRIHS','DATA SCIENCE','A',90)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Aditya','Gen ai','A',90)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Saurabh','MBA','A',95)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Karan','Computer science','A',96)''')
cursor.execute(''' INSERT INTO STUDENT VALUES('Kshitija','Agriculture','A',90)''')

## dislay all the records
print("The inserted records are")
cursor.execute("""SELECT * FROM STUDENT""")
for row in cursor:
    print(row)

# commit your changes in the database
connection.commit()
connection.close()