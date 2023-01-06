#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test, http
import ssl
import sys


class RequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == "__main__":
    server_address = ("localhost", 3000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile="server.pem",
        ssl_version=ssl.PROTOCOL_TLS,
    )
    httpd.serve_forever()
