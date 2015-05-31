#!/usr/bin/python3
import curses
from lib import get_peers_ as get
#  from lib import Conversation as Chat

#  cbreak - dont wait for ENTER
#  \x12 == ^R

def chooser(stdscr):
    nicks, ips = get()
    curses.cbreak()
    stdscr.scrollok(True)
    while True:
        global key
        key = stdscr.getkey()
        stdscr.addstr(str(key))
        stdscr.refresh()
        break
    curses.endwin()


def main(stdscr):
    chooser(stdscr)

try:
    curses.wrapper(main)
except KeyboardInterrupt:
    pass
