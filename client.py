from http.client import HTTPConnection
import json

server_addr = '46.101.152.181:8080'
APP_PORT = 1652
BUFF = 4096

def post_nick(nick='ivan'):
    """
    nick: str
    post your nickname to remote server
    """
    con = HTTPConnection(server_addr)
    header = {'Content-type': 'text/plain'}
    con.request('POST','',bytes(nick, 'utf-8'), header)
    con.close()

def get_peers():
    """
    retuns dict of peers from server
    keys : values
    IP : NICK
    NICK : IP
    """
    con = HTTPConnection(server_addr)
    con.request('GET', '')
    response = con.getresponse()

    #print(response.status)
    d = json.loads(response.read().decode('utf-8'))
    #print(type(d))
    return d

def listener(conn):
    while True:
        yield str(conn.recv(BUFF), 'utf-8')

class Sender(object):
    def __init__(self, IP):
        self.conn = socket.connect((IP, APP_PORT))
    def __call__(self,msg):
        self.conn.send(msg.encode('utf-8'))

if __name__ == '__main__':
    post_nick()
    print(get_peers())
