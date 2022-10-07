import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="********"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE if not exists Banking_Project")
# mycursor.execute("CREATE Table if not exists Account_details (user_name varchar(10
# If this page is executed with no error, you have successfully created a database.
