# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/victorgarric/Documents/INVENTAIRE/principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMenuBar, QStatusBar, QMessageBox, QProgressDialog, QFileDialog


import display 
import cursor 
import listing
import excel
import delete
import manual
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 262)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_find_id = QPushButton(self.centralwidget)
        self.button_find_id.setGeometry(QtCore.QRect(370, 10, 110, 32))
        self.button_find_id.setObjectName(_fromUtf8("button_find_id"))
        self.button_find_name = QPushButton(self.centralwidget)
        self.button_find_name.setGeometry(QtCore.QRect(370, 50, 110, 32))
        self.button_find_name.setObjectName(_fromUtf8("button_find_name"))
        self.button_find_cas = QPushButton(self.centralwidget)
        self.button_find_cas.setGeometry(QtCore.QRect(370, 90, 110, 32))
        self.button_find_cas.setObjectName(_fromUtf8("button_find_cas"))
        self.button_find_vpid = QPushButton(self.centralwidget)
        self.button_find_vpid.setGeometry(QtCore.QRect(370, 130, 110, 32))
        self.button_find_vpid.setObjectName(_fromUtf8("button_find_cas"))

        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(150, 180, 110, 32))
        self.button_add.setObjectName(_fromUtf8("button_add"))

        self.button_stop = QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(150, 210, 110, 32))
        self.button_stop.setObjectName(_fromUtf8("button_stop"))

        self.button_invent = QPushButton(self.centralwidget)
        self.button_invent.setGeometry(QtCore.QRect(20, 180, 120, 32))
        self.button_invent.setObjectName(_fromUtf8("button_invent"))

        self.button_invent_2 = QPushButton(self.centralwidget)
        self.button_invent_2.setGeometry(QtCore.QRect(20, 210, 120, 32))
        self.button_invent_2.setObjectName(_fromUtf8("button_invent_2"))

        self.button_delete = QPushButton(self.centralwidget)
        self.button_delete.setGeometry(QtCore.QRect(260, 210, 120, 32))
        self.button_delete.setObjectName(_fromUtf8("button_delete"))

        self.button_manual = QPushButton(self.centralwidget)
        self.button_manual.setGeometry(QtCore.QRect(260, 180, 120, 32))
        self.button_manual.setObjectName(_fromUtf8("button_delete"))  

        self.button_repop = QPushButton(self.centralwidget)
        self.button_repop.setGeometry(QtCore.QRect(380, 195, 110, 32))
        self.button_repop.setObjectName(_fromUtf8("button_repop"))     


        self.line_id = QLineEdit(self.centralwidget)
        self.line_id.setGeometry(QtCore.QRect(90, 10, 251, 21))
        self.line_id.setObjectName(_fromUtf8("line_id"))
        self.line_name = QLineEdit(self.centralwidget)
        self.line_name.setGeometry(QtCore.QRect(90, 50, 251, 21))
        self.line_name.setObjectName(_fromUtf8("line_name"))
        self.line_cas = QLineEdit(self.centralwidget)
        self.line_cas.setGeometry(QtCore.QRect(90, 90, 251, 21))
        self.line_cas.setObjectName(_fromUtf8("line_cas"))
        self.line_vpid = QLineEdit(self.centralwidget)
        self.line_vpid.setGeometry(QtCore.QRect(90, 130, 251, 21))
        self.line_vpid.setObjectName(_fromUtf8("line_cas"))       
        self.label_id = QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(10, 10, 56, 13))
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 50, 56, 13))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_cas = QLabel(self.centralwidget)
        self.label_cas.setGeometry(QtCore.QRect(10, 90, 56, 13))
        self.label_cas.setObjectName(_fromUtf8("label_cas"))
        self.label_vpid = QLabel(self.centralwidget)
        self.label_vpid.setGeometry(QtCore.QRect(10, 130, 56, 13))
        self.label_vpid.setObjectName(_fromUtf8("label_cas"))       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connection
        #self.trigger=QtCore.pyqtSignal()
        #self.trigger.connect(self.button_add, QtCore.SIGNAL("released()"), self.new)
        #self.connect(self.button_stop, QtCore.SIGNAL("released()"), self.quit)
        #self.connect(self.button_find_id, QtCore.SIGNAL("released()"), self.find_id)
        #self.connect(self.button_find_name, QtCore.SIGNAL("released()"), self.find_name)
        #self.connect(self.button_find_vpid, QtCore.SIGNAL("released()"), self.find_vpid)
        #self.connect(self.button_find_cas, QtCore.SIGNAL("released()"), self.find_cas)
        #self.connect(self.button_invent, QtCore.SIGNAL("released()"), self.invent)
        #self.connect(self.button_invent_2, QtCore.SIGNAL("released()"), self.invent_2)
        #self.connect(self.button_delete, QtCore.SIGNAL("released()"), self.delete)
        #self.connect(self.button_manual, QtCore.SIGNAL("released()"), self.manu)
        #self.connect(self.button_repop, QtCore.SIGNAL("released()"), self.repop)
        self.button_stop.clicked.connect(self.quit)
        self.button_add.clicked.connect(self.new)
        self.button_find_id.clicked.connect(self.find_id)
        self.button_find_name.clicked.connect(self.find_name)
        self.button_find_vpid.clicked.connect(self.find_vpid)
        self.button_find_cas.clicked.connect(self.find_cas)
        self.button_invent.clicked.connect(self.invent)
        self.button_invent_2.clicked.connect(self.invent_2)
        self.button_delete.clicked.connect(self.delete)
        self.button_manual.clicked.connect(self.manu)
        self.button_repop.clicked.connect(self.repop)

    def invent(self) :
        prog=QProgressDialog("Compiling inventory...","Cancel",0,100,self)
        prog.open()
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        curs.execute("""SELECT * FROM "main"."chem" WHERE "id" > 0 """)
        store=curs.fetchall()
        a=excel.makeinvent(store)
        a.begin()
        internal=0
        if prog.wasCanceled() :
                return None
        while internal != 100 :
            try :
                internal=(a.returnid()/len(store))*100
            except :
                internal=100
            prog.setValue(internal)
            if prog.wasCanceled() :
                return None
        b=a.returnbook()
        try :  
            fname=QFileDialog.getSaveFileName(self, 'Save File', '/','Excel File (*.xls)')[0]
            b.save(fname)
            QMessageBox.information(self, "Info", "Inventory was saved sucessfully.")
            if prog.wasCanceled() :
                return None
        except :
            QMessageBox.information(self, "Info", "Inventory was no saved.")

    def invent_2 (self) :

        prog=QProgressDialog("Compiling inventory...","Cancel",0,100,self)
        prog.open()
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        curs.execute("""SELECT "storage" FROM "main"."chem" WHERE "id" > 0 """)
        store=curs.fetchall()
        newstore=[]
        count=-1
        if prog.wasCanceled() :
                return None
        for i in store :
            count=count+1
            if i[0] not in newstore :
                newstore.append(store[count][0])

        a=excel.makeinvent_2(newstore)
        a.begin()
        internal=[0,1]
        percent=0
        if prog.wasCanceled() :
                return None
        while percent != 100 :
            internal=(a.returnid())
            try :
                percent=((internal[0]/internal[1])*100)
            except :
                percent=100
            prog.setValue(percent)
            if prog.wasCanceled() :
                return None
        b=a.returnbook()
        try :  
            fname=QFileDialog.getSaveFileName(self, 'Save File', '/','Excel File (*.xls)')[0]
            b.save(fname)
            QMessageBox.information(self, "Info", "Inventory was saved sucessfully.")
        except :
            QMessageBox.information(self, "Info", "Inventory was no saved.")





    def new (self) :

        self.prop=display.Ui_chem()
        curs=cursor.connection()[0]
        curs.execute('''SELECT MAX(id) FROM chem''')
        maximum=curs.fetchone()[0]
        maximum=int(maximum)
        if maximum==-1 :
            maximum=0
        self.prop.line_id.setText(str(maximum+1))
        self.prop.line_id.setReadOnly(True)
        self.prop.show()


    def find_id (self) :
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        idfind=str(self.line_id.text())
        idfind=(idfind,)
        curs.execute('''SELECT * FROM chem WHERE id=?''', idfind)
        data.commit()
        data.commit()
        store=curs.fetchone()
        if str(self.line_id.text())=="-1" :
            store=None
        data.close()
        if store != None :
            self.line_id.setText('')
            self.prop=display.Ui_chem()
            self.prop.line_name.setText(store[0])
            self.prop.line_vendor.setText(store[1])
            self.prop.line_vpid.setText(store[2])
            self.prop.line_cas.setText(store[3])
            self.prop.line_size.setText(store[4])
            self.prop.line_storage.setText(store[5])
            self.prop.line_room.setText(store[6])
            self.prop.line_id.setText(str(store[7]))
            self.prop.line_id.setReadOnly(True)
            self.prop.show()
        else :
            self.line_id.setText('')           
            QMessageBox.information(self, "Error", "ID doesn't exist")
            data.close()

    def find_vpid (self) :
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        idfind=str(self.line_vpid.text())
        idfind=(idfind,)
        curs.execute('''SELECT * FROM chem WHERE vpid=?''', idfind)
        data.commit()
        data.commit()
        store=curs.fetchone()
        print(store[0])
        if store[0]=="CHEMDB\n" or store[0]=='CHEMDB' :
            store=None
        data.close()
        if store != None :
            self.line_id.setText('')
            self.prop=display.Ui_chem()
            self.prop.line_name.setText(store[0])
            self.prop.line_vendor.setText(store[1])
            self.prop.line_vpid.setText(store[2])
            self.prop.line_cas.setText(store[3])
            self.prop.line_size.setText(store[4])
            self.prop.line_storage.setText(store[5])
            self.prop.line_room.setText(store[6])
            self.prop.line_id.setText(str(store[7]))
            self.prop.line_id.setReadOnly(True)
            self.prop.show()
        else :
            self.line_id.setText('')           
            QMessageBox.information(self, "Error", "Vendor ID doesn't exist")
            data.close()

    def delete (self) :

        self.prop=delete.Ui_delete_entries()
        self.prop.show()

    def find_name (self) :
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        idfind=str(self.line_name.text())
        idfind.lower()
        idfind="%"+idfind+"%"
        idfind=(idfind,)
        curs.execute('''SELECT "name", "id", "storage" FROM "main"."chem" where "name" LIKE ? LIMIT 0, 100''', idfind)
        data.commit()
        store=curs.fetchall()
        for item in store :
            if item[0]=="CHEMDB\n" or item[0]=="CHEMDB" :
                store.remove(item)
        if store != None and len(store)==1 :
            curs.execute('''SELECT * FROM "main"."chem" where "name" LIKE ? LIMIT 0, 100''', idfind)
            data.commit()
            store=curs.fetchall()
            for item in store :
                if item[0]=="CHEMDB\n" or item[0]=="CHEMDB" :
                    store.remove(item)
            data.close()
            self.line_name.setText('')
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

        elif store != None and len(store)>1 :
            self.listing=listing.Ui_Form()
            self.listing.list.clear()
            reform=[]
            for produit in range(len(store)) :
                reform.append(str(store[produit][0])+" // STORE : "+ str(store[produit][2]) +" // ID : " + str(store[produit][1]))
                self.listing.list.addItem(reform[produit])
            data.close()
            if len(store)>=99 :
                QMessageBox.information(self, "Warning", "More than 100 references were found. Only displaying the first 100 records")
            self.line_name.setText('')
            self.listing.show()

        else :
            data.close()
            self.line_name.setText('')
            QMessageBox.information(self, "Error", "The research gave nothing back")

    def find_cas (self) :
        allconn=cursor.connection()
        curs=allconn[0]
        data=allconn[1]
        casfind=str(self.line_cas.text())
        casfind.lower()
        casfind=(casfind,)
        curs.execute('''SELECT * FROM "main"."chem" WHERE "cas"=?''', casfind)
        store=curs.fetchone()
        if store[0]=="CHEMDB\n" or store[0]=='CHEMDB' :
            store=None
        if store!=None :
            self.prop=display.Ui_chem()
            self.prop.line_name.setText(store[0])
            self.prop.line_vendor.setText(store[1])
            self.prop.line_vpid.setText(store[2])
            self.prop.line_cas.setText(store[3])
            self.prop.line_size.setText(store[4])
            self.prop.line_storage.setText(store[5])
            self.prop.line_room.setText(store[6])
            self.prop.line_id.setText(str(store[7]))
            self.prop.line_id.setReadOnly(True)
            self.line_cas.setText('')
            self.prop.show()

        else :
            QMessageBox.information(self, "Error", "Cannot found CAS")
            self.line_cas.setText('')
            data.close()

    def repop (self) :
        h=QMessageBox.question(self, "WARNING", "WARNING ! Repopulate will erase all the database by an Excel file generated by this database. Do not do this action randomly !!! Are you sur you want to continue ?")
        if h==QMessageBox.No :
            return None
        fname=QFileDialog.getOpenFileName(self, 'Choose an Excel File', '/','Excem File (*.xls)')[0]
        prog=QProgressDialog("Gathering Data...","Cancel",0,100,self)
        prog.open()
        if prog.wasCanceled() :
            return None
        rep=excel.repopulate(fname)
        try :
            rep.begin()
            if prog.wasCanceled() :
                return None
        except :
            return None
        state=int(rep.returnstate())
        prog.setLabelText("Repopulating...")
        while state==0 :
            prog.setValue(rep.returnpercent())
            state=rep.returnstate()
            prog.setCancelButton(None)
        if state==1 :
            prog.close()
            QMessageBox.information(self, "Sucess", "Repopulation Sucess")
        if state==-1 :
            QMessageBox.information(self, "Error", "Repopulation Failled")

    def abort(self) :
        return None


    def manu (self) :
        self.load=manual.Ui_manual()
        self.load.show()

    def quit (self) :
        QApplication.quit()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chem Database", None))
        self.button_find_id.setText(_translate("MainWindow", "Find ID", None))
        self.button_find_vpid.setText(_translate("MainWindow", "Find Vendor ID", None))
        self.button_repop.setText(_translate("MainWindow", "Repopulate", None))
        self.button_find_name.setText(_translate("MainWindow", "Find Name", None))
        self.button_find_cas.setText(_translate("MainWindow", "Find CAS", None))
        self.button_add.setText(_translate("MainWindow", "Add Entry", None))
        self.button_stop.setText(_translate("MainWindow","Close Program",None))
        self.button_invent.setText(_translate("MainWindow","Inventory:Full",None))
        self.button_invent_2.setText(_translate("MainWindow","Inventory:Group",None))
        self.button_delete.setText(_translate('MainWindow','Delete Entries',None))
        self.button_manual.setText(_translate('MainWindow','Manual CMD',None))
        self.label_id.setText(_translate("MainWindow", "ID", None))
        self.label_name.setText(_translate("MainWindow", "Name", None))
        self.label_cas.setText(_translate("MainWindow", "CAS", None))
        self.label_vpid.setText(_translate("MainWindow", "Vendor ID", None))


