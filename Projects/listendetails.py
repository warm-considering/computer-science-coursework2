from PyQt4 import uic, QtGui
import settings
import editlistens
import deletelistens
import pyodbc
( Ui_listendetails, QDialog ) = uic.loadUiType( 'listendetails.ui' )

class listendetails ( QDialog ):
    """listendetails inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_listendetails()
        self.ui.setupUi( self )
    def populate(self):
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Listens")
        row = cursor.fetchall()
        cnxn.close()
        for item in row:
            rowcount = self.ui.listentable.rowCount()
            self.ui.listentable.insertRow(rowcount)
            self.ui.listentable.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
            self.ui.listentable.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
            self.ui.listentable.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(item[2])))
            self.ui.listentable.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
            self.ui.listentable.setItem(rowcount, 4,QtGui.QTableWidgetItem(str(item[4])))
            self.ui.listentable.setItem(rowcount, 5,QtGui.QTableWidgetItem(str(item[5])))
    def __del__ ( self ):
        self.ui = None
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = settings.settings(self)
        load.show()
    def edit(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = editlistens.editlistens(self)
        load.show()
    def clear(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = deletelistens.deletelistens(self)
        load.show()
