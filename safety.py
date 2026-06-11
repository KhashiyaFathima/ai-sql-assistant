def is_safe_query(sql):

    blocked_keywords = [
        "DELETE",
        "UPDATE",
        "INSERT",
        "DROP",
        "ALTER",
        "TRUNCATE",
        "ATTACH",
        "PRAGMA"
    ]

    sql_upper = sql.upper().strip()

    if not sql_upper.startswith("SELECT"):
        return False

    for keyword in blocked_keywords:
        if keyword in sql_upper:
            return False

    return True