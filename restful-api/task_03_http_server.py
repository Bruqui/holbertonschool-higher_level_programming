import http.server
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler to demonstrate how to handle GET requests
    and serve text and JSON responses using Python's http.server module.
    """


    def do_GET(self):
        """
        Handles GET requests. Based on the endpoint accessed, the method
        will respond with either a text message, JSON data, or an error
        message.
        """
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(data.encode())
        
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())
        
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("404 Not Found".encode())

def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
