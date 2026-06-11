# AI SQL Assistant

## Overview

AI SQL Assistant converts natural language questions into SQL queries, executes them on a SQLite database, and returns results with a plain-English explanation.

## Features

* Natural Language to SQL using Gemini AI
* SQLite database integration
* SQL safety validation
* Business-friendly result explanations
* FastAPI REST API
* Structured JSON responses

## Project Structure

ai_sql_project/

* app.py
* sql_generator.py
* db.py
* safety.py
* explainer.py
* schema.sql
* database.db
* requirements.txt

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --reload
```

## API Endpoint

POST /query

Request:

```json
{
  "question": "Show all products"
}
```

Response:

```json
{
  "sql": "SELECT * FROM products;",
  "results": [],
  "explanation": "..."
}
```

## Technologies Used

* Python
* FastAPI
* SQLite
* Google Gemini API
