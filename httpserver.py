from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os

ADDRESS = "127.0.0.1"
PORT = 8080
FILEDIR = os.getcwd() + "/html/"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/" == self.path or "/main" == self.path :
            with open( FILEDIR + 'main.html', 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                self.requestline
        elif "/sub" == self.path :
            with open( FILEDIR + 'sub.html', 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                self.requestline
        else:
            self.send_error(404)
        return

httpd = ThreadingHTTPServer((ADDRESS, PORT), MyHandler)
httpd.serve_forever()
