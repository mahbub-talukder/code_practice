import requests
from requests.auth import HTTPBasicAuth

# Define the JSON-RPC request payload
payload = {
    "jsonrpc": "2.0",
    "method": "add_numbers",
    "params": {"x": 5, "y": 3},
    "id": 1
}

# Define the authentication credentials
USERNAME = "user"
PASSWORD = "password"

# Send the JSON-RPC request to the server with authentication
response = requests.post(
    "http://localhost:8001",
    json=payload,
    auth=HTTPBasicAuth(USERNAME, PASSWORD)
).json()

# Print the result received from the server
if "result" in response:
    print("Result:", response["result"])
else:
    print("Error:", response["error"])
