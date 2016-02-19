# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/victorgarric/Documents/INVENTAIRE/display.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
import cursor
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

class Ui_chem(QWidget):

    def __init__(self):

        super(Ui_chem, self).__init__()
        self.initUi(self)

    def initUi(self, chem):
        chem.setObjectName(_fromUtf8("chem"))
        chem.resize(601, 430)
        self.pushButton = QPushButton(chem)
        self.pushButton.setGeometry(QtCore.QRect(340, 390, 110, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QPushButton(chem)
        self.pushButton_2.setGeometry(QtCore.QRect(449, 390, 151, 32))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.line_name = QLineEdit(chem)
        self.line_name.setGeometry(QtCore.QRect(140, 40, 431, 31))
        self.line_name.setObjectName(_fromUtf8("line_name"))
        self.label_name = QLabel(chem)
        self.label_name.setGeometry(QtCore.QRect(30, 50, 56, 13))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.line_vendor = QLineEdit(chem)
        self.line_vendor.setGeometry(QtCore.QRect(140, 100, 211, 21))
        self.line_vendor.setObjectName(_fromUtf8("line_vendor"))
        self.label_vendor = QLabel(chem)
        self.label_vendor.setGeometry(QtCore.QRect(30, 100, 56, 13))
        self.label_vendor.setObjectName(_fromUtf8("label_vendor"))
        self.line_vpid = QLineEdit(chem)
        self.line_vpid.setGeometry(QtCore.QRect(140, 140, 211, 21))
        self.line_vpid.setObjectName(_fromUtf8("line_vpid"))
        self.label_vpid = QLabel(chem)
        self.label_vpid.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.label_vpid.setObjectName(_fromUtf8("label_vpid"))
        self.line_cas = QLineEdit(chem)
        self.line_cas.setGeometry(QtCore.QRect(140, 200, 211, 21))
        self.line_cas.setObjectName(_fromUtf8("line_cas"))
        self.label_cas = QLabel(chem)
        self.label_cas.setGeometry(QtCore.QRect(30, 210, 111, 16))
        self.label_cas.setObjectName(_fromUtf8("label_cas"))
        self.line_size = QLineEdit(chem)
        self.line_size.setGeometry(QtCore.QRect(140, 250, 211, 21))
        self.line_size.setObjectName(_fromUtf8("line_size"))
        self.label_size = QLabel(chem)
        self.label_size.setGeometry(QtCore.QRect(30, 250, 111, 16))
        self.label_size.setObjectName(_fromUtf8("label_size"))
        self.label_storage = QLabel(chem)
        self.label_storage.setGeometry(QtCore.QRect(30, 310, 111, 16))
        self.label_storage.setObjectName(_fromUtf8("label_storage"))
        self.label_room = QLabel(chem)
        self.label_room.setGeometry(QtCore.QRect(320, 310, 111, 16))
        self.label_room.setObjectName(_fromUtf8("label_room"))
        self.line_storage = QLineEdit(chem)
        self.line_storage.setGeometry(QtCore.QRect(90, 300, 211, 21))
        self.line_storage.setObjectName(_fromUtf8("line_storage"))
        self.line_room = QLineEdit(chem)
        self.line_room.setGeometry(QtCore.QRect(370, 300, 211, 21))
        self.line_room.setObjectName(_fromUtf8("line_room"))
        self.line_id = QLineEdit(chem)
        self.line_id.setGeometry(QtCore.QRect(370, 350, 211, 21))
        self.line_id.setObjectName(_fromUtf8("line_id"))
        self.label_id = QLabel(chem)
        self.label_id.setGeometry(QtCore.QRect(320, 350, 111, 16))
        self.label_id.setObjectName(_fromUtf8("label_id"))


        self.retranslateUi(chem)
        QtCore.QMetaObject.connectSlotsByName(chem)

        #connections
        #self.connect(self.pushButton, QtCore.SIGNAL("released()"), self.save)
        #self.connect(self.pushButton_2, QtCore.SIGNAL("released()"), self.quit)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.quit)

    def save (self) :
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        name=str(self.line_name.text())
        vendor=str(self.line_vendor.text())
        vpid=str(self.line_vpid.text())
        cas=str(self.line_cas.text())
        size=str(self.line_size.text())
        storage=str(self.line_storage.text())
        room=str(self.line_room.text())
        idnum=str(self.line_id.text())
        idtupl=(idnum,)
        val=(name,vendor,vpid,cas,size,storage,room,idnum)
        curs.execute('''DELETE FROM chem WHERE id=?''', idtupl)
        data.commit()
        curs.execute('''INSERT INTO chem VALUES (?,?,?,?,?,?,?,?)''', val)
        data.commit()
        data.close()
        self.close()

    def quit (self) :
        self.close()





    def retranslateUi(self, chem):
        chem.setWindowTitle(_translate("chem", "Displaying Product", None))
        self.pushButton.setText(_translate("chem", "Save", None))
        self.pushButton_2.setText(_translate("chem", "Quit without saving", None))
        self.label_name.setText(_translate("chem", "Name", None))
        self.label_vendor.setText(_translate("chem", "Vendor", None))
        self.label_vpid.setText(_translate("chem", "Vendor Catalog ID", None))
        self.label_cas.setText(_translate("chem", "CAS", None))
        self.label_size.setText(_translate("chem", "Container Size", None))
        self.label_storage.setText(_translate("chem", "Storage", None))
        self.label_room.setText(_translate("chem", "Room", None))
        self.label_id.setText(_translate("chem","ID",None))

