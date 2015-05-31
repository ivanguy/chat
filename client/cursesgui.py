import curses
import client

# curses.echo - print pressed simbols
# curses.cbreak - read ech key on press, not waiting for enter hit
class Chooser(object):
    '''
    choose a peer to chat with
    '''
    stdscr = None
    win = None
    peers = None

    def curses_start(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.win = curses.newwin(
                5 + self.w_height,
                self.w_width,
                2,
                4)

    def curses_stop(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()
