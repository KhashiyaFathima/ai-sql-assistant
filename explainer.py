import google.generativeai as genai

import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def explain_results(question, results):

    prompt = f"""
    User Question:
    {question}

    Query Results:
    {results}

    Explain the results in simple business language.
    """

    response = model.generate_content(prompt)

    return response.text