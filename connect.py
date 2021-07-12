import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode"
)

if db.is_connected():
  print("Success connected database!")