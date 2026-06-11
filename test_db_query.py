from db import execute_sql

sql = "SELECT * FROM customers"

results = execute_sql(sql)

print(results)