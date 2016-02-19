# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import principal
import sqlite3 as sql
import cursor
import xlrd
import classes
class principal(QMainWindow, principal.Ui_MainWindow):
    def __init__(self, parent=None):
        super(principal, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()
        curs=cursor.connection()




if __name__=='__main__':
    app = QApplication(sys.argv)
    principal = principal()
    principal.main()
    app.exec_()