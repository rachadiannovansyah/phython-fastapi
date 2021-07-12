import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode",
  database="py_product"
)

cursor = db.cursor()
sql = """CREATE TABLE product (
  id INT AUTO_INCREMENT PRIMARY KEY,
  productName VARCHAR(255),
  description Varchar(255),
  price Integer(12),
  stock Varchar(255)
)
"""
cursor.execute(sql)

print("Product table has been successfully created!")