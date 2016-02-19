# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/victorgarric/Documents/INVENTAIRE/list.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton
import cursor 
import display
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

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.initUi(self)

    def initUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(527, 336)
        self.label_info = QLabel(Form)
        self.label_info.setGeometry(QtCore.QRect(170, 10, 201, 21))
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.list = QListWidget(Form)
        self.list.setGeometry(QtCore.QRect(30, 40, 481, 251))
        self.list.setObjectName(_fromUtf8("list"))
        self.button_view = QPushButton(Form)
        self.button_view.setGeometry(QtCore.QRect(200, 300, 110, 32))
        self.button_view.setObjectName(_fromUtf8("button_view"))
        self.button_quit = QPushButton(Form)
        self.button_quit.setGeometry(QtCore.QRect(410, 300, 110, 32))
        self.button_quit.setObjectName(_fromUtf8("button_quit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #self.connect(self.button_quit, QtCore.SIGNAL("released()"), self.quit)
        #self.connect(self.button_view, QtCore.SIGNAL("released()"), self.view)
        self.button_view.clicked.connect(self.view)
        self.button_quit.clicked.connect(self.quit)

    def quit (self) :
        self.close()

    def view (self) :
        current=self.list.selectedItems()
        current=current[0]
        current_text=str(current.text())
        current_text=current_text.split(" // ID : ")
        current_text=current_text[1]
        current_text=(current_text,)

        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        curs.execute('''SELECT * FROM "main"."chem" where "id"=?''', current_text)
        data.commit()
        store=curs.fetchall()
        data.close()
        self.prop=display.Ui_chem()
        self.prop.line_name.setText(store[0][0])
        self.prop.line_vendor.setText(store[0][1])
        self.prop.line_vpid.setText(store[0][2])
        self.prop.line_cas.setText(store[0][3])
        self.prop.line_size.setText(store[0][4])
        self.prop.line_storage.setText(store[0][5])
        self.prop.line_room.setText(store[0][6])
        self.prop.line_id.setText(str(store[0][7]))
        self.prop.line_id.setReadOnly(True)
        self.prop.show()
        self.close()       
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Name Found", None))
        self.label_info.setText(_translate("Form", "More than one id were found...", None))
        self.button_view.setText(_translate("Form", "View", None))
        self.button_quit.setText(_translate("Form", "Quit", None))

