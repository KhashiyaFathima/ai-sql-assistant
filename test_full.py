from sql_generator import generate_sql
from db import execute_sql

question = "Show all customers"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

results = execute_sql(sql)

print("\nResults:")
print(results)