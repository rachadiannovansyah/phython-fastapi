import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE py_product")

print("Database has been successfully created!")