from safety import is_safe_query

print(is_safe_query("SELECT * FROM customers"))
print(is_safe_query("DROP TABLE customers"))