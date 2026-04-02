import http.server, ssl, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

server = http.server.HTTPServer(('0.0.0.0', 443), http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('rivian.com+1.pem', 'rivian.com+1-key.pem')
server.socket = ctx.wrap_socket(server.socket, server_side=True)
print('Serving HTTPS on https://rivian.com')
server.serve_forever()
