import xmlrpc.client

# Define the XML-RPC server URL
server_url = "http://localhost:8000/RPC2"

# Define the authentication credentials
USERNAME = "user"
PASSWORD = "password"

# Create an XML-RPC server proxy with authentication
proxy = xmlrpc.client.ServerProxy(server_url, verbose=True)
proxy._ServerProxy__transport.user_agent += f" ({USERNAME}:{PASSWORD})"

# Call the remote function
result = proxy.add_numbers(5, 3)
print("Result:", result)
