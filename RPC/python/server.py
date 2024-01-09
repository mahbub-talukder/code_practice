from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8100),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Define the function to be called remotely
    def add_numbers(x, y):
        return x + y

    # Register the function
    server.register_function(add_numbers, 'add_numbers')

    # Run the server
    print("RPC remote server listening on port 8100...")
    server.serve_forever()
