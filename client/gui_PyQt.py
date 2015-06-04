# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys

class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setFixedSize(1000, 600)
        self.setWindowTitle("CHAT")

        self.login_input_label = QtGui.QLabel("<b>Login:</b>")
        self.login_input_label.setTextFormat(2)
        self.login_input = QtGui.QLineEdit()
        self.peers_list = QtGui.QComboBox()
        self.peers_list.addItems(['friend1', 'friend2', 'friend3', 'friend4'])
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
        self.msg_input_panel.setContentsMargins(20,0,20,0)
        self.msg_input_panel.addWidget(self.msg_input)
        self.msg_input_panel.addWidget(self.send_msg_button)

        self.wrapper = QtGui.QVBoxLayout()
        self.wrapper.addLayout(self.setting_box)
        self.wrapper.addWidget(self.chat_window, alignment=QtCore.Qt.AlignCenter)
        self.wrapper.addLayout(self.msg_input_panel)

        self.setLayout(self.wrapper)

    def send_msg(self):
        pass

    def receive_msg(self):
        pass

    def start_chating(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_w = MainWidget()
    main_w.show()
    sys.exit(app.exec_())