from PyQt4 import uic, QtGui
import edituserdetails
import userdetail
import pickle
import pyodbc
( Ui_edituser, QDialog ) = uic.loadUiType( 'edituser.ui' )
def search(self):
    sentby = self.sender()
    print("sent by "+sentby.objectName())
    if sentby.objectName() == "viewbutton":
        try:
            searchterm = int(self.ui.useridbox.text())
            print(str(searchterm))
            pickle.dump( searchterm, open( "searchterm.temp", "wb"))
        except:
            QtGui.QMessageBox.about(self, 'Error', 'That is not a number')
            return
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserID = ?",int(searchterm))
        row = cursor.fetchall()
        cnxn.close()
        if len(row) == 1:
            self.close()
            load = edituserdetails.edituserdetails(self)
            load.show()
        else:
            QtGui.QMessageBox.about(self, 'Error', 'Entry not found')
    elif sentby.objectName() == "viewbutton2":
        try:
            searchterm = self.ui.usernamebox.text()
            print(str(searchterm))
            pickle.dump( searchterm, open( "searchterm.temp", "wb"))
        except:
            QtGui.QMessageBox.about(self, 'Error', 'An Unknown Error has occured')
            return
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Users WHERE Username = ?",str(searchterm))
        row = cursor.fetchall()
        cnxn.close()
        if len(row) >0:
            self.close()
            load = edituserdetails.edituserdetails(self)
            load.show()
        else:
            QtGui.QMessageBox.about(self, 'Error', 'Entry not found')
class edituser ( QDialog ):
    """edituser inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_edituser()
        self.ui.setupUi( self )
    
    def __del__ ( self ):
        self.ui = None
    def view(self):
        search(self)
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = userdetail.userdetail(self)
        load.show()