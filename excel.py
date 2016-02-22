# -*- coding: utf-8 -*-
from xlwt import Workbook
from xlwt import Borders
import xlrd
from PyQt5 import QtCore
import cursor
class makeinvent (QtCore.QThread):

	def __init__(self, listing) :

		self.list=listing
		self.nextid=0
		self.book=Workbook()		
		super(makeinvent, self).__init__() 

	def begin (self) :
		self.statusTh = makeinvent(self)
		self.start()

	def run (self) :

		feuil1 = self.book.add_sheet('inventory')
		borders = Borders()
		feuil1.col(0).width = 10000
		feuil1.col(2).width = 5000
		feuil1.col(5).width = 5000
		feuil1.write(0,0,'Name')
		feuil1.write(0,1,'Vendor')
		feuil1.write(0,2,'Id in Vendor Catalog')
		feuil1.write(0,3,'CAS')
		feuil1.write(0,4,'Size')
		feuil1.write(0,5,'Storage')
		feuil1.write(0,6,'Room')
		feuil1.write(0,7,'Id')
		feuil1.write(0,8,'This file has been automaticaly generated from the chemistry database.')

		self.nextid=0

		for itera in range(len(self.list)) :
			self.nextid=self.nextid+1
			ligne=feuil1.row(self.nextid)
			ligne.write(0,self.list[itera][0])
			ligne.write(1,self.list[itera][1])
			ligne.write(2,self.list[itera][2])
			ligne.write(3,self.list[itera][3])
			ligne.write(4,self.list[itera][4])
			ligne.write(5,self.list[itera][5])
			ligne.write(6,self.list[itera][6])
			ligne.write(7,self.list[itera][7])


	def returnid (self) :
		return self.nextid

	def returnbook (self) :
		return self.book


class makeinvent_2 (QtCore.QThread):

	def __init__(self, listing) :

		self.list=listing
		self.nextid=0
		self.book=Workbook()
		self.percent=[]
		self.percent.append(0)
		self.percent.append(len(self.list))
		super(makeinvent_2, self).__init__() 

	def begin (self) :
		self.statusTh = makeinvent(self)
		self.start()

	def run (self) :
		for i in range(len(self.list)) :
			itema=self.book.add_sheet(self.list[i]+"_area_"+str(i))
			itema.col(0).width = 10000
			itema.col(2).width = 5000
			itema.col(5).width = 5000
			itema.write(0,0,'Name')
			itema.write(0,1,'Vendor')
			itema.write(0,2,'Id in Vendor Catalog')
			itema.write(0,3,'CAS')
			itema.write(0,4,'Size')
			itema.write(0,5,'Storage')
			itema.write(0,6,'Room')
			itema.write(0,7,'Id')
			itema.write(0,8,'This file has been automaticaly generated from the chemistry database.')
			tupleitem=(str(self.list[i]),)
			self.nextid=0
			allconn=cursor.connection()
			curs=allconn[0]
			data=allconn[1]
			curs.execute("""SELECT * FROM "main"."chem" WHERE "storage"=? """,tupleitem)
			totin=curs.fetchall()
			itema=self.interin(itema,totin,self.nextid)
			self.percent[0]=self.percent[0]+1





	def interin (self,itema,totin,nextid) :
		for itera in range(len(totin)) :
			self.nextid=self.nextid+1
			ligne=itema.row(self.nextid)
			ligne.write(0,totin[itera][0])
			ligne.write(1,totin[itera][1])
			ligne.write(2,totin[itera][2])
			ligne.write(3,totin[itera][3])
			ligne.write(4,totin[itera][4])
			ligne.write(5,totin[itera][5])
			ligne.write(6,totin[itera][6])
			ligne.write(7,totin[itera][7])	
		return itema	


	def returnid (self) :
		return self.percent

	def returnbook (self) :
		return self.book

class repopulate (QtCore.QThread):

	def __init__(self, filex) :

		self.file=filex
		self.book=Workbook()
		self.total=0	
		self.ret=0	
		super(repopulate, self).__init__() 

	def begin (self) :
		self.statusTh = repopulate(self)
		self.start()

	def run (self) :
		wb = xlrd.open_workbook(self.file)
		sh = wb.sheet_by_name(u'inventory')
		temp=[]
		for rownum in range(sh.nrows) :
			temp.append(sh.row_values(rownum))
		temp.pop(0)
		for item in range(len(temp)) :
			temp[item][7]=str(int(temp[item][7]))
		allconn=cursor.connection()
		curs=allconn[0]
		data=allconn[1]
		curs.execute("""DELETE FROM "main"."chem" WHERE "id">0 """)
		data.commit()
		maximum=0
		for i in range(len(temp)) :
			if int(temp[i][7]) > maximum :
				maximum=int(temp[i][7])
		try :
			for item in range(len(temp)) :
				finin=(temp[item][0],temp[item][1],temp[item][2],temp[item][3],temp[item][4],temp[item][5],temp[item][6],temp[item][7])
				curs.execute('''INSERT INTO "main"."chem" VALUES (?,?,?,?,?,?,?,?)''', finin)
				data.commit()
				self.ret=((int(temp[item][7])*100)/maximum)
			self.total=1

		except :
			self.total=-1

	def returnstate (self) :
		return self.total
	def returnpercent (self) :
		return self.ret







