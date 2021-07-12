import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode",
  database="py_product"
)

cursor = db.cursor()
sql = "INSERT INTO product (productName, description, price, stock) VALUES (%s, %s, %s, %s)"
value = ("Laptop", "ASUS Tech", 6800000, "10")
cursor.execute(sql, value)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))