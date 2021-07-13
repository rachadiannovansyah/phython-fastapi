import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode",
  database="py_product"
)

cursor = db.cursor()
sql = "SELECT * FROM product"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)