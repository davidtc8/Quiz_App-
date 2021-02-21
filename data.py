import requests

# Parameters for the API
parameter = {
    "amount": 10,
    "category": 27,
    "type": "boolean",
}

# Getting the API Information
response = requests.get(url = "https://opentdb.com/api.php?amount=10&category=27&type=boolean", params= parameter)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print(question_data)