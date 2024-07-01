import mysql.connector
def connect():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tiger",
    database="newproject"
    )
    return mydb