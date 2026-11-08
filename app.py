from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os

APP_VERSION = os.getenv("APP_VERSION", "v1")

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Healthy")
            return

        hostname = socket.gethostname()

        html = f"""
        <html>
        <head>
            <title>Cloud Demo Dashboard</title>
            <style>
                body {{
                    font-family: Arial;
                    background: #eef4ff;
                    text-align: center;
                    padding: 60px;
                }}
                .card {{
                    background: white;
                    padding: 35px;
                    margin: auto;
                    max-width: 550px;
                    border-radius: 15px;
                }}
                h1 {{ color: #1769aa; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Cloud Demo Dashboard</h1>
                <p>Status: Healthy</p>
                <p>Version: {APP_VERSION}</p>
                <p>Instance: {hostname}</p>
            </div>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Cloud Demo application started on port 8000")

server.serve_forever()