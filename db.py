import mysql.connector
def connection():
    conn=mysql.connector.connect(

        host="localhost",
        user="root",
        password="root",
        database="student_management1"
    )
    return conn
if(connection()):
    print("connection establish successfully")
else:
    print("connection failled")