import sqlite3

connection = sqlite3.connect("invoices.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
  print(row)

connection.close()
