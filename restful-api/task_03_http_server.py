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
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))
        
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status_data = {"status": "OK"}
            json_data = json.dumps(status_data)
            self.wfile.write(json_data.encode('utf-8'))
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_data = {"error": "Endpoint not found"}
            json_data = json.dumps(error_data)
            self.wfile.write(json_data.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """
    Starts the HTTP server on the specified port and binds it to the given
    handler class to manage incoming requests.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
