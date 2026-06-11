import google.generativeai as genai

import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_sql(question):

    prompt = f"""
    Database Schema:

    customers(id,name,email,city,created_at)
    products(id,name,category,price)
    orders(id,customer_id,product_id,quantity,order_date)

    Convert the question into SQLite SQL.

    Question:
    {question}

    Return only SQL.
    """

    response = model.generate_content(prompt)
    print("RAW RESPONSE:")

    print(response.text)

    sql = response.text.strip()


    sql = sql.replace("```sqlite", "")
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()