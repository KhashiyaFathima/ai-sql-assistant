from fastapi import FastAPI
from pydantic import BaseModel

from sql_generator import generate_sql
from db import execute_sql
from safety import is_safe_query
from explainer import explain_results

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI SQL Assistant Running"}

@app.post("/query")
def query(data: QueryRequest):

    try:
        sql = generate_sql(data.question)

        if not is_safe_query(sql):
            return {
                "error": "Unsafe SQL query detected"
            }

        results = execute_sql(sql)

        explanation = explain_results(
            data.question,
            results
        )

        return {
            "sql": sql,
            "results": results,
            "explanation": explanation
        }

    except Exception as e:
        return {
            "error": str(e)
        }