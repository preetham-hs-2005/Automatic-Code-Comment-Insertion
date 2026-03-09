import requests
import json

url = "http://127.0.0.1:8001/api/generate"
payload = {
    "code": """def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result"""
}
headers = {'Content-Type': 'application/json'}

try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", json.dumps(response.json(), indent=2))
except Exception as e:
    print("Error:", e)
