import mysql.connector
# This is mysql connector to connect mysql server
mydb = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="Ajeet@1234#",
    db="Banking_Project"
    )
# Cursor objects interact with the MySQL server using a MySQLConnection object
mycursor = mydb.cursor()