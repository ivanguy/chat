from http.client import HTTPConnection
import json
import re
import threading
from socket import socket
# import queue
from time import sleep


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
    con.request('POST', '', nick, header)
    con.getresponse()
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
    con.close()
    return d


def get_peers_():
    """
    -> (nicks, ips)
    split mixed tuple into two separate ones
    """
    mix = get_peers()
    nicks = dict()
    ips = dict()
    ipv4 = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}$')  # this regex mathes ipv4
    for item in mix:
        if ipv4.match(item):
            ips[item] = mix[item]
        else:
            nicks[item] = mix[item]
    return nicks, ips


class Conversation:

    """
    a chat object
    use:

    in_stream - generator -> incoming messages

    out_stream <- outgoing messages

    """
    def __init__(self, nick='{username}'):
        """
        ip: str '000.000.000.000'

        makes incoming and outgoing connections in a non-blocking way
        """
        self.nick = nick
        self.in_socket = None
        self.out_socket = None
        self.nicks, self.ips = get_peers_()

        post_nick(nick)
        self.start_updater()

    def start_updater(self):
        """
        !BLOCKING
        """
        def updater():
            while True:
                sleep(10)
                self.nicks, self.ips = get_peers_()
                if self.out_socket == None:
                    print(*list(self.nicks.keys()), sep='\n')

        updater_thread = threading.Thread(target=updater, daemon=True)
        updater_thread.start()


    def server(self, key=None):
        """
        sets in_socket
        !BLOCKING
        """
        #"""
        #это генератор, будет выдавать ник подключающегося друга(или ip недруга)
        #ждет вызова do_i_trust_him
        #блокирующий генератор => в тред его
        #
        #key = c :пока не разрешить кому-нибудь подключиться - будет крутиться
        #"""
        server_sock = socket()
        server_sock.bind(("", APP_PORT))
        server_sock.listen(1)
        print('listening on {}'.format(APP_PORT))

        #while True:
            # accept connection from exact IP
        conn, addr = server_sock.accept()
        print('accepted {}'.format(addr))
        print('...but do i trust him?....')
        print('yes, for now..')
        #   try:
        #       yield self.ips[addr(0)]
        #   except KeyError:
        #       yield addr[0]
        #       queue.get()
        #   if self.trust:
        self.in_socket = conn
        server_sock.close()
        #       break
        #    else:
        #        conn.close()
        #else:  # выполнится когда рак на горе свиснет
        #    server_sock.close()

    def out_connect(self, nick):
        """
        sets out_socket: connection for outgoing messages
        """
        client_sock = socket()
        client_sock.settimeout(15)
        while True:
            try:
                ip = self.nicks[nick]
                port = APP_PORT
                print('trying to connect {}:{}'.format(ip, port))
                client_sock.connect((str(ip), APP_PORT))
                self.out_socket = client_sock
                print('connected!!')
                break
            except OSError:
                print('connection timeout')
                continue

    def in_stream(self):
        """
        incoming messages generator + buffering
        """
        while True:
            if self.in_socket is None:
                yield '...тишина...'
                sleep(10)
            else:
                msg = ''
                while True:
                    data = self.in_socket.recv(BUFF)
                    if not data:
                        break
                    msg = msg + data.decode('utf-8')
                yield msg

    def out_stream(self, msg):
        """
        sends msg to peer
        """
        if self.out_socket is None:
            print('self.out_socket is None')
        else:
            self.out_socket.send(msg.encode('utf-8'))
