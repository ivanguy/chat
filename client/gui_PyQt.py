# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
import lib

class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setFixedSize(1000, 600)
        self.setWindowTitle("CHAT")

        self.login_input_label = QtGui.QLabel("<b>Login:</b>")
        self.login_input_label.setTextFormat(2)
        self.login_input = QtGui.QLineEdit()
        self.peers_list = QtGui.QComboBox()
        self.peers_list.addItems(list(self.get_peers_list().keys()))
        self.start_button = QtGui.QPushButton("Start chatting")

        self.chat_window = QtGui.QLabel('<center>WELCOME!</center>')
        self.chat_window.setFixedSize(940, 450)
        self.chat_window.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Plain)

        self.msg_input = QtGui.QTextEdit()
        self.send_msg_button = QtGui.QPushButton("Send")

        self.setting_box = QtGui.QHBoxLayout()
        self.setting_box.addWidget(self.login_input_label)
        self.setting_box.addWidget(self.login_input)
        self.setting_box.addWidget(self.peers_list)
        self.setting_box.addWidget(self.start_button)

        self.msg_input_panel = QtGui.QHBoxLayout()
        self.msg_input_panel.setSpacing(10)
        self.msg_input_panel.setContentsMargins(20, 0, 20, 0)
        self.msg_input_panel.addWidget(self.msg_input)
        self.msg_input_panel.addWidget(self.send_msg_button)

        self.wrapper = QtGui.QVBoxLayout()
        self.wrapper.addLayout(self.setting_box)
        self.wrapper.addWidget(self.chat_window, alignment=QtCore.Qt.AlignCenter)
        self.wrapper.addLayout(self.msg_input_panel)

        self.setLayout(self.wrapper)
        self.connect(self.start_button, QtCore.SIGNAL("clicked()"), self.start_chatting)
        self.connect(self.login_input, QtCore.SIGNAL("editingFinished()"), self.post_nick)

    # def keyPressEvent(self, event):
    #     if event.key() == QtCore.Qt.Key_Enter:
    #         self.emit()

    def post_nick(self):
        nick = self.login_input.text()
        lib.post_nick(nick)

    def get_peers_list(self):
        nick, peers = lib.get_peers_()
        return nick

    def send_msg(self):
        pass

    def receive_msg(self):
        pass

    def start_chatting(self):

        con = lib.Conversation()
        self.chat_window.setText('started...')



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_w = MainWidget()
    main_w.show()
    sys.exit(app.exec_())