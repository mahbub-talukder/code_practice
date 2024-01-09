from  xmlrpc.client import ServerProxy

# Create an XML-RPC client
proxy = ServerProxy("http://localhost:8100/RPC2")
print("proxy-->", proxy)
# Call the remote function
result = proxy.add_numbers(5, 3)
print("Result:", result)
