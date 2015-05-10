#!/usr/bin/python3
peers = dict()
count = 0
from http.server import BaseHTTPRequestHandler, HTTPServer
import json,urllib.request

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self, content_type='text/html'):
        global count
        count += 1
        print('#'*10)
        print('Received {} connection #{}'.format(self.command, count))
        print(self.client_address)
        #print(self.headers.__dict__)

        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self): #todo
        self.do_HEAD('text/plain')
        ip = self.client_address[0]
        jsondata = json.dumps(peers)
        self.wfile.write(bytes(jsondata, 'utf-8'))
        print('sent ', jsondata,' to {}@{}'.format(peers[ip],ip))

    def do_POST(self):
        self.do_HEAD()

        ip = self.client_address[0]
        nick = self.rfile.read(self.headers['Content-lenght']).decode('utf-8')
        
        if ip in peers.keys():
            peers.pop(ip) # delete existing name
        peers[ip] = nick
        print('Added {} @ {}'.format(nick, ip))
        print(peers)



host = ''
port = 8080

try:
    server = HTTPServer((host, port), Handler)
    print(server.server_name,'@',str(urllib.request.urlopen('http://www.biranchi.com/ip.php').read()),':',server.server_port)
    server.serve_forever()
except KeyboardInterrupt:
    print('Shutting down on ^C')
    server.server_close()
