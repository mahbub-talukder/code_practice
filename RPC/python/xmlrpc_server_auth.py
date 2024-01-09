from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Define the authentication credentials
USERNAME = "user"
PASSWORD = "password"

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

    def authenticate(self, headers):
        username, password = headers.get("Authorization", "").split(":")
        return username == USERNAME and password == PASSWORD

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Define the function to be called remotely
    def add_numbers(x, y):
        return x + y

    # Register the function
    server.register_function(add_numbers, 'add_numbers')

    # Run the server
    print("Server listening on port 8000...")
    server.serve_forever()
