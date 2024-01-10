from  xmlrpc.client import ServerProxy,SafeTransport
from base64 import b64encode

# XML-RPC API endpoint
api_url = "http://10.172.16.4:3000/rpc"

# Your username and password for Basic Authentication
username = 'devops'
password = 'devOps@321#'
# Create a Basic Authentication header encryption text value
credentials = f'{username}:{password}'
credentials_encoded = b64encode(credentials.encode('utf-8')).decode('utf-8')
print("credentials_encoded-->", credentials_encoded)

headers = {
            'Authorization': f'Basic {credentials}',
            'Content-Type': 'application/xml',
            'Accept': 'application/json'
           
           }

# Create an XML-RPC server proxy with Basic Authentication headers
server = ServerProxy(api_url, headers=[('Authorization',f'Basic {credentials}')])

# Make an XML-RPC API call (replace 'methodName' and 'params' with actual values)
# try:
result = server.get_software_information()
print(result)
# except Exception as e:
#     print(f"Error: {e}")
