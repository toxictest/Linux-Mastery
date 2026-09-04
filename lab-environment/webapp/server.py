from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(
            json.dumps(
                {
                    "app": "Linux-Mastery-Lab",
                    "status": "healthy",
                    "endpoints": ["/api/users", "/api/audit"],
                }
            ).encode()
        )


HTTPServer(("0.0.0.0", 3000), App).serve_forever()
