# -*- coding: utf-8 -*-
import sqlite3 as sql
import os



global is1
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QMenuBar, QStatusBar, QMessageBox, QProgressDialog, QFileDialog
config=open('data/configure')
config=config.readlines()
result={}
for info in range(len(config)) :
	temp=config[info].split('=')
	temp[1]=temp[1].split('\n')[0]
	result[temp[0]]=temp[1]
path=result['db']
def connection() :
	try :
		db=sql.connect(path, timeout=5)
		cursor=db.cursor()
		return (cursor,db)
	except :
		return None

def connection2(path) :
	try :
		db=sql.connect(path, timeout=5)
		cursor=db.cursor()
		return (cursor,db)
	except :
		return None

def verif(path) :
	get=connection2(path)
	get[0].execute('''SELECT * FROM "main"."chem" WHERE "id"=-1''')
	result=get[0].fetchone()
	try :
		if result[0]=='CHEMDB' and result[-1]==-1 :
			return True
		else :
			return False
	except :
		return False

