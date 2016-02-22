# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/victorgarric/Documents/INVENTAIRE/delete.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLabel, QMessageBox
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

class Ui_delete_entries(QWidget):
    def __init__(self):

        super(Ui_delete_entries, self).__init__()
        self.initUi(self)

    def initUi (self, delete_entries):
        delete_entries.setObjectName(_fromUtf8("delete_entries"))
        delete_entries.resize(472, 239)
        self.button_exit = QPushButton(delete_entries)
        self.button_exit.setGeometry(QtCore.QRect(350, 200, 110, 32))
        self.button_exit.setObjectName(_fromUtf8("button_exit"))
        self.button_delete = QPushButton(delete_entries)
        self.button_delete.setGeometry(QtCore.QRect(240, 200, 110, 32))
        self.button_delete.setObjectName(_fromUtf8("button_delete"))
        self.edit = QTextEdit(delete_entries)
        self.edit.setGeometry(QtCore.QRect(20, 50, 431, 141))
        self.edit.setObjectName(_fromUtf8("edit"))
        self.label = QLabel(delete_entries)
        self.label.setGeometry(QtCore.QRect(60, 0, 431, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QLabel(delete_entries)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 431, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(delete_entries)
        QtCore.QMetaObject.connectSlotsByName(delete_entries)

        #self.connect(self.button_exit, QtCore.SIGNAL("released()"), self.exit)
        #self.connect(self.button_delete, QtCore.SIGNAL("released()"), self.suppression)
        self.button_exit.clicked.connect(self.exit)
        self.button_delete.clicked.connect(self.suppression)

    def exit(self) :
        self.close()

    def suppression (self) :
        liste=self.edit.toPlainText()
        liste=str(liste)
        liste=liste.split(",")
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        erreur=[]
        for i in range(len(liste)) :
            temp=liste[i]
            temp=(temp,)
            curs.execute('''SELECT * FROM "chem" WHERE id=?''',temp)
            inout=curs.fetchone()

            if inout == None :
                erreur.append(liste[i])
            else :
                curs.execute('''DELETE FROM "chem" WHERE id=?''', temp)
                data.commit()

        data.close()
        if len(erreur)==0 :
            QMessageBox.information(self, "Succes", "All specified ID were deleted")
        if len(erreur)!=0 :
            QMessageBox.information(self, "Error", "Following ID were not deleted \n %s" % erreur)


    def retranslateUi(self, delete_entries):
        delete_entries.setWindowTitle(_translate("delete_entries", "Delete Entries", None))
        self.button_exit.setText(_translate("delete_entries", "Exit", None))
        self.button_delete.setText(_translate("delete_entries", "Delete", None))
        self.label.setText(_translate("delete_entries", " Write all ID you want to delete separated by commas.", None))
        self.label_2.setText(_translate("delete_entries", "WARNING : There is no way to cancel this action !!", None))

