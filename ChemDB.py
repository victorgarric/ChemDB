# -*- coding: utf-8 -*-
import main
import sys
import shutil
import os
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QFileDialog, QSplashScreen
import cursor

#Tempory windows which initiate the program, checking for database and configuration file
class tempwin(object):
    def setupUi(self, MainWindow):
        self.hide()
class tempapp(QMainWindow, tempwin):
    def __init__(self,parent=None):
        #splash screen initialisation
        self.splash_pix = QPixmap('data/loading.jpg')
        self.splash = QSplashScreen(self.splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        self.splash.setMask(self.splash_pix.mask())
        self.splash.show()

        super(tempapp, self).__init__(parent)
        self.setupUi(self)
    def main(self):
        #launching program
        self.hide()
        self.launch()
    def launch(self):
        #reading configuration
        config=open('data/configure')
        config=config.readlines()
        envir=main.principal
        self.result={}
        for info in range(len(config)) :
            temp=config[info].split('=')
            temp[1]=temp[1].split('\n')[0]
            self.result[temp[0]]=temp[1]

        if self.result['db']=='' :
            #if no databatse, asking user for creating/pointing
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
            #if already configured : checking if the DB still exist
            if os.path.exists(self.result['db'])==True :
                None
            else :
                #if db do not exist : delete configuration and reboot program
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
            #launching program if all checkpoints are ok
            self.splash.hide()
            prog=main.principal()
            prog.main()
            sys.exit(app.exec_())
    def loaddb (self) :
        #loading db file
        fname=QFileDialog.getOpenFileName(self, 'Choose a DB', '/','SQLite Databse (*.sqlite)')[0]
        if fname=='' :
            z=QMessageBox(parent=self, text="No DB has been selected, closing program")
            z.exec_()
            z.exec_()
            self.terminer()
        isvalid=cursor.verif(str(fname))
        #checking is the DB is valid
        if isvalid==False :
            z=QMessageBox(parent=self, text="Wrong File/File Corruption. \nClosing programm")
            z.exec_()
            self.terminer()
        else :
            #writiing new configuration
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
        #new db creation
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
