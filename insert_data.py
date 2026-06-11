import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO customers
VALUES(1,'John','john@gmail.com','Chennai','2024-01-01')
""")

cursor.execute("""
INSERT INTO products
VALUES(1,'Laptop','Electronics',50000)
""")

cursor.execute("""
INSERT INTO orders
VALUES(1,1,1,2,'2025-05-15')
""")

conn.commit()
conn.close()

print("Data inserted")