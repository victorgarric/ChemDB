# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/victorgarric/Documents/INVENTAIRE/manual.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import cursor
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QLabel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_manual(QWidget):
    def __init__(self):

        super(Ui_manual, self).__init__()
        self.initUi(self)

    def initUi(self, manual):
        manual.setObjectName(_fromUtf8("manual"))
        manual.resize(588, 209)
        self.plainTextEdit = QPlainTextEdit(manual)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 571, 121))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.button_quit = QPushButton(manual)
        self.button_quit.setGeometry(QtCore.QRect(460, 170, 110, 32))
        self.button_quit.setObjectName(_fromUtf8("button_quit"))
        self.button_execute = QPushButton(manual)
        self.button_execute.setGeometry(QtCore.QRect(360, 170, 110, 32))
        self.button_execute.setObjectName(_fromUtf8("button_execute"))
        self.label = QLabel(manual)
        self.label.setGeometry(QtCore.QRect(10, 10, 561, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(manual)
        QtCore.QMetaObject.connectSlotsByName(manual)

        #self.connect(self.button_quit, QtCore.SIGNAL("released()"), self.quit)
        #self.connect(self.button_execute, QtCore.SIGNAL("released()"), self.launchcmd)
        self.button_quit.clicked.connect(self.quit)
        self.button_execute.clicked.connect(self.launchcmd)

    def quit (self) :
        self.close()

    def launchcmd (self) :
        cmd=self.plainTextEdit.toPlainText()
        cmd=str(cmd)
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        try :
            curs.execute(cmd)
            data.commit()
            data.close()
            self.plainTextEdit.setPlainText('')
            QMessageBox.information(self, "Success", "Command executed sucessfully")
        except :
            QMessageBox.information(self, "Error", "Bad Command : Databse operation interrupted")



    def retranslateUi(self, manual):
        manual.setWindowTitle(_translate("manual", "Manual Input", None))
        self.button_quit.setText(_translate("manual", "Quit", None))
        self.button_execute.setText(_translate("manual", "Execute", None))
        self.label.setText(_translate("manual", "WARNING ! : Manual inputs are very dangerous and can lead to a dramatic database collapse !", None))

