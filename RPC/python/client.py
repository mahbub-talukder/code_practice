from  xmlrpc.client import ServerProxy
USERNAME = 'devops'
PASSWORD = 'devOps@321#'
server_url = "http://10.172.16.4:3000/rpc"
# Create an XML-RPC client
proxy = ServerProxy(server_url,verbose=True)
proxy._ServerProxy__transport.user_agent += f" ({USERNAME}:{PASSWORD})"

print("proxy-->", proxy)
# Call the remote function
result = proxy.get_software_information()
print("Result:", result)
