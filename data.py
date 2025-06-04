import mysql.connector
def connection():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bankingsystem3"
    )
    return conn
if (connection()):
    print("connection established")
else:
    print("connection failed")