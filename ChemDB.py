# -*- coding: utf-8 -*-
import main
import sys
import shutil
import time
import os
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QMenuBar, QStatusBar, QMessageBox, QProgressDialog, QFileDialog, QSplashScreen
import cursor

class tempwin(object):
    def setupUi(self, MainWindow):
        self.hide()
class tempapp(QMainWindow, tempwin):
    def __init__(self,parent=None):

        self.splash_pix = QPixmap('data/loading.jpg')
        self.splash = QSplashScreen(self.splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        self.splash.setMask(self.splash_pix.mask())
        self.splash.show()

        super(tempapp, self).__init__(parent)
        self.setupUi(self)
    def main(self):
        self.hide()
        self.launch()
    def launch(self):
        #lecture de la configuration
        config=open('data/configure')
        config=config.readlines()
        envir=main.principal
        self.result={}
        for info in range(len(config)) :
            temp=config[info].split('=')
            temp[1]=temp[1].split('\n')[0]
            self.result[temp[0]]=temp[1]

        if self.result['db']=='' :
            h=QMessageBox(parent=self, text="No DB has been pointed. \nDo you want to create a new database or to load an existing database ?")
            h.addButton(QPushButton('Close'), QMessageBox.YesRole)
            h.addButton(QPushButton('Load an Existing DB'), QMessageBox.NoRole)
            h.addButton(QPushButton('New DB'), QMessageBox.HelpRole)
            self.splash.hide()
            tot = h.exec_()
            if tot==0 :
                self.terminer()
            if tot==1 :
                self.loaddb()
            if tot==2 :
                self.newdb()
        else :
            if os.path.exists(self.result['db'])==True :
                None
            else :
                self.splash.hide()
                h=QMessageBox(parent=self, text="Corrupted file or non existent : Deleting configuration")
                self.result['db']=""
                new_conf=''
                for i in self.result :
                    new_conf+='%s=%s\n' % (i,self.result[i])
                config=open('data/configure','w')
                config.write(new_conf)
                config.close()
                h.exec_()
                python = sys.executable
                os.execl(python, python, * sys.argv)
            self.splash.hide()
            prog=main.principal()
            prog.main()
            sys.exit(app.exec_())
    def loaddb (self) :
        fname=QFileDialog.getOpenFileName(self, 'Choose a DB', '/','SQLite Databse (*.sqlite)')[0]
        if fname=='' :
            z=QMessageBox(parent=self, text="No DB has been selected, closing program")
            z.exec_()
            z.exec_()
            self.terminer()
        isvalid=cursor.verif(str(fname))
        if isvalid==False :
            z=QMessageBox(parent=self, text="Wrong File/File Corruption. \nClosing programm")
            z.exec_()
            self.terminer()
        else :
            self.result['db']=str(fname)
            new_conf=''
            for i in self.result :
                new_conf+='%s=%s\n' % (i,self.result[i])
            config=open('data/configure','w')
            config.write(new_conf)
            config.close()
            python = sys.executable
            os.execl(python, python, * sys.argv)
    def terminer (self) :
        #QApplication.quit()
        #sys.exit(app.exec_())
        sys.exit(0)

    def newdb (self) :
        fname=QFileDialog.getSaveFileName(self, 'Create a DB', '/','SQLite Databse (*.sqlite)')[0]
        shutil.copy('data/model.sqlite',fname)
        self.result['db']=str(fname)
        new_conf=''
        for i in self.result :
            new_conf+='%s=%s\n' % (i,self.result[i])
        config=open('data/configure','w')
        config.write(new_conf)
        config.close()
        python = sys.executable
        os.execl(python, python, * sys.argv)
app = QApplication(sys.argv)
tempapp=tempapp()
tempapp.main()
app.exec_()
