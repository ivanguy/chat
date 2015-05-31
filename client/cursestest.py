#!/usr/bin/python3
import curses
from client import get_peers_
import threading
from socket import socket

nicks, ips = get_peers_()

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    
    out_lines = curses.LINES - curses.LINES//3
    in_lines = curses.LINES - out_lines

    outwin = stdscr.derwin(out_lines, curses.COLS, 0, 0)
    inwin = stdscr.derwin(in_lines, curses_COLS, out_lines, 0)

    l_thread = threading.Thread(server)
    l_thread.daemon(True)
    l_thread.start()

def server():
    listen_sock = socket()
    listen_sock.bind(('', 1652))
    listen_sock.listen(1)
    while True:
        conn_in = listen_sock.accept()
        if conn_in.getpeername() in ips:
            in_msg = threading.Thread(printer, args=(conn_in))
            in_msg.daemon(True)
            in_msg.start()
        else:
            conn_in.close()

def printer(conn):
    nick = conn.getpeername()[0]
    while True:
        msg = conn.recv(4096)
        inwin.addstr(nick + ':' + msg)




curses.wrapper(main)
