from jsonrpcserver import methods, serve
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import Unauthorized

# Define the authentication credentials
USERNAME = "user"
PASSWORD = "password"

# Authentication decorator
def authenticate(func):
    def wrapper(data, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise Unauthorized(description="Authentication required")

        username, password = auth_header.split(":")
        if username == USERNAME and password == PASSWORD:
            return func(data, request)
        else:
            raise Unauthorized(description="Invalid credentials")

    return wrapper

# Define a method that adds two numbers
@methods.add
@authenticate
def add_numbers(data, request):
    x = data["x"]
    y = data["y"]
    return x + y

# Start the JSON-RPC server
if __name__ == "__main__":
    serve(methods=methods, host="localhost", port=8001)
