from http.client import HTTPConnection
import json
import re
import threading
from socket import socket


server_addr = '46.101.152.181:8080'
APP_PORT = 1652
BUFF = 4096


def post_nick(nick='{username}'):
    """
    nick: str
    post your nickname to remote server
    """
    nick = '{' + nick + '}'
    con = HTTPConnection(server_addr)
    header = {'Content-type': 'text/plain'}
    con.request('POST', '', bytes(nick, 'utf-8'), header)
    con.close()


def get_peers():
    """
    use get_peers_
    retuns dict of peers from server
    keys : values
    IP : NICK
    NICK : IP
    """
    con = HTTPConnection(server_addr)
    con.request('GET', '')
    response = con.getresponse()
    d = json.loads(response.read().decode('utf-8'))
    return d


def get_peers_():
    """
    -> (nicks, ips)
    split mixed tuple into two separate ones
    """
    nicks = get_peers()
    ips = dict()
    ipv4 = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}$')  # this regex mathes ipv4
    for item in nicks:
        if ipv4.match(item):
            ips[item] = nicks.pop(item)
    return nicks, ips


class Conversation:
    """
    a chat object
    use:

    in_stream - generator -> incoming messages

    out_stream <- outgoing messages

    """
    def __init__(self, ip, nick='{username}'):
        """
        ip: str '000.000.000.000'

        makes incoming and outgoing connections in a non-blocking way
        """
        self.i_conn = None      # REMEMBER setting theese two takes some time
        self.o_conn = None
        self.quit_flag = 0
        self.nick = nick

        def out_connect(ip):
            """
            sets o_conn: connection for outgoing messages
            """
            client_sock = socket()
            while not self.quit_flag:
                try:
                    client_sock.settimeout(5)
                    client_sock.connect((str(ip), APP_PORT))
                    self.o_conn = client_sock
                except socket.timeout:
                    continue

        def in_connect(ip):
            """
            sets i_conn: a connection for incoming messages
            """
            server_sock = socket()
            server_sock.bind(("", APP_PORT))
            server_sock.listen(1)
            while not self.quit_flag:
                # accept connection from exact IP
                conn = server_sock.accept()
                if str(conn.getpeername()[0]) == str(ip):
                    self.i_conn = conn
                    server_sock.close()
                    break
                else:
                    conn.close()
            else:
                server_sock.close()

        out_thread = threading.Thread(out_connect, daemon=True, args=(ip))
        in_thread = threading.Thread(in_connect, daemon=True, args=(ip))
        out_thread.start()
        in_thread.start()

    def in_stream(self):
        """
        incoming messages generator + buffering
        """
        while not self.quit_flag:
            msg = ''
            while True:
                data = self.i_conn.recv(BUFF)
                if not data:
                    break
                msg = msg + data.decode('utf-8')
            yield msg

    def out_stream(self, msg):
        """
        sends msg to peer
        """
        self.o_conn.send(msg.encode('utf-8'))
