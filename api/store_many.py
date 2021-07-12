import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode",
  database="py_product"
)

cursor = db.cursor()
sql = "INSERT INTO product (productName, description, price, stock) VALUES (%s, %s, %s, %s)"
values = [
    ("Laptop", "ASUS Tech", 6800000, "10"),
    ("Monitor", "ASUS Tech", 1500000, "10"),
    ("Keyboard", "ASUS Tech", 760000, "10"),
    ("Mouse", "ASUS Tech", 350000, "10")
]

for value in values:
    cursor.execute(sql, value)
    db.commit()

print("{} data ditambahkan".format(len(values)))