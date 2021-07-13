import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sedekahcode",
  database="py_product"
)

cursor = db.cursor()
sql = "DELETE from product WHERE id=%s"
value = (1, )
cursor.execute(sql, value)

db.commit()

print("{} data has been successfully deleted".format(cursor.rowcount))