import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode",
  database="py_product"
)

cursor = db.cursor()
sql = "UPDATE product SET productName=%s, description=%s, price=%s, stock=%s WHERE id=%s"
value = ("Laptop", "Lenovo", 72000000, "10", 1)
cursor.execute(sql, value)

db.commit()

print("{} data has been successfully updated".format(cursor.rowcount))