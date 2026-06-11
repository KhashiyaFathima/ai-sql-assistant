import sqlite3

def execute_sql(sql):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(sql)

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    results = []

    for row in rows:
        results.append(dict(zip(columns, row)))

    conn.close()

    return results