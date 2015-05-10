from http.client import HTTPConnection
import json

server_addr = '46.101.152.181:8080'

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
    con = HTTPConnection(server_addr)
    con.request('GET', '')
    response = con.getresponse()

    print(response.status)
    d = json.loads(response.read().decode('utf-8'))
    print(type(d))
    return d

if __name__ == '__main__':
    post_nick()
    print(get_peers())
