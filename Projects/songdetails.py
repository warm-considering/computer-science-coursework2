from PyQt4 import uic, QtGui
import pyodbc
import addsongs
import editsong
import settings
( Ui_songdetails, QDialog ) = uic.loadUiType( 'songdetails.ui' )

class songdetails ( QDialog ):
    """songdetails inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_songdetails()
        self.ui.setupUi( self )
    def populate(self):
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Songs")
        row = cursor.fetchall()
        cnxn.close()
        for item in row:
            rowcount = self.ui.songtable.rowCount()
            self.ui.songtable.insertRow(rowcount)
            self.ui.songtable.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
            self.ui.songtable.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
            self.ui.songtable.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(item[2])))
            self.ui.songtable.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
            self.ui.songtable.setItem(rowcount, 4,QtGui.QTableWidgetItem(str(item[4])))
            self.ui.songtable.setItem(rowcount, 5,QtGui.QTableWidgetItem(str(item[5])))
            self.ui.songtable.setItem(rowcount, 6,QtGui.QTableWidgetItem(str(item[6])))
            self.ui.songtable.setItem(rowcount, 7,QtGui.QTableWidgetItem(str(item[7])))
            self.ui.songtable.setItem(rowcount, 8,QtGui.QTableWidgetItem(str(item[8])))
            self.ui.songtable.setItem(rowcount, 9,QtGui.QTableWidgetItem(str(item[9])))
            self.ui.songtable.setItem(rowcount, 10,QtGui.QTableWidgetItem(str(item[10])))
            self.ui.songtable.setItem(rowcount, 11,QtGui.QTableWidgetItem(str(item[11])))
            self.ui.songtable.setItem(rowcount, 12,QtGui.QTableWidgetItem(str(item[12])))
            self.ui.songtable.setItem(rowcount, 13,QtGui.QTableWidgetItem(str(item[13])))
            self.ui.songtable.setItem(rowcount, 14,QtGui.QTableWidgetItem(str(item[14])))
            self.ui.songtable.setItem(rowcount, 15,QtGui.QTableWidgetItem(str(item[15])))
            self.ui.songtable.setItem(rowcount, 16,QtGui.QTableWidgetItem(str(item[16])))
            self.ui.songtable.setItem(rowcount, 17,QtGui.QTableWidgetItem(str(item[17])))
            self.ui.songtable.setItem(rowcount, 18,QtGui.QTableWidgetItem(str(item[18])))
            self.ui.songtable.setItem(rowcount, 19,QtGui.QTableWidgetItem(str(item[19])))
    def __del__ ( self ):
        self.ui = None
    def add(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = addsongs.addsongs(self)
        load.show()
    def edit(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = editsong.editsong(self)
        load.show()
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = settings.settings(self)
        load.show()