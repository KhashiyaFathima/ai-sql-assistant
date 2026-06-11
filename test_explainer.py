from explainer import explain_results

results = [
    {
        "id": 1,
        "name": "John",
        "city": "Chennai"
    }
]

print(explain_results("Show all customers", results))