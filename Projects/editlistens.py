from PyQt4 import uic, QtGui
import editlistensdetails
import listendetails
import pyodbc
import pickle
( Ui_editlistens, QDialog ) = uic.loadUiType( 'editlistens.ui' )
searchterm = 0
class editlistens ( QDialog ):
    """editlistens inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_editlistens()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def search(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        try:
            global searchterm
            searchterm = int(self.ui.listenidbox.text())
            pickle.dump( searchterm, open( "searchterm.temp", "wb"))
        except:
            QtGui.QMessageBox.about(self, 'Error', 'That is not a number')
            return
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Listens WHERE ListenID = ?",str(searchterm))
        row = cursor.fetchall()
        cnxn.close()
        if len(row) == 1:
            self.close()
            load = editlistensdetails.editlistensdetails(self)
            load.show()
        else:
            QtGui.QMessageBox.about(self, 'Error', 'Entry not found')


    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = listendetails.listendetails(self)
        load.show()