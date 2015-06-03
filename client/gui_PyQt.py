# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

class MainWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1000, 600)
        self.setWindowTitle("CHAT")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_w = MainWidget()
    main_w.show()
    sys.exit(app.exec_())