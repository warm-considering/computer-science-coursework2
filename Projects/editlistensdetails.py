from PyQt4 import uic, QtGui
import pickle
import editlistens
import pyodbc
( Ui_editlistensdetails, QDialog ) = uic.loadUiType( 'editlistensdetails.ui' )
searchterm = ""
def populate(self):
    searchterm = pickle.load(open("searchterm.temp", "rb"))
    print(str(searchterm))
    self.ui.listenidbox.setText(str(searchterm))
    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Listens WHERE ListenID = ?",str(searchterm))
    row = cursor.fetchone()
    cnxn.close()
    self.ui.songidbox.setText(str(row[1]))
    self.ui.useridbox.setText(str(row[2]))
    self.ui.nooflistensbox.setText(str(row[3]))
    self.ui.ratingbox.setText(str(row[4]))
    self.ui.lastlistenbox.setText(str(row[5]))
class editlistensdetails ( QDialog ):
    """editlistensdetails inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_editlistensdetails()
        self.ui.setupUi( self )
        populate(self)
        


    def __del__ ( self ):
        self.ui = None
    def confirm(self):
        try:
            sentby = self.sender()
            print("sent by "+sentby.objectName())
            cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
            cursor = cnxn.cursor()
            cursor.execute("UPDATE Listens SET SongID = ? WHERE ListenID = ?",self.ui.songidbox.text(),self.ui.listenidbox.text())
            cursor.execute("UPDATE Listens SET UserID = ? WHERE ListenID = ?",self.ui.useridbox.text(),self.ui.listenidbox.text())
            cursor.execute("UPDATE Listens SET NoOfListen = ? WHERE ListenID = ?",self.ui.nooflistensbox.text(),self.ui.listenidbox.text())
            cursor.execute("UPDATE Listens SET Rating = ? WHERE ListenID = ?",self.ui.ratingbox.text(),self.ui.listenidbox.text())
            cursor.execute("UPDATE Listens SET LastListen = ? WHERE ListenID = ?",self.ui.lastlistenbox.text(),self.ui.listenidbox.text())
            cursor.commit()
            cnxn.close()
            QtGui.QMessageBox.about(self, 'Success', 'The data has been changed')
        except:
            QtGui.QMessageBox.about(self, 'Error', 'An error has occured')
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = editlistens.editlistens(self)
        load.show()
    def delete(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Are you sure that you want to delete your messages?")
        msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        msgBox.setDefaultButton(QtGui.QMessageBox.No)
        ret = msgBox.exec_()
        if ret == QtGui.QMessageBox.Yes:
            try:
                cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=:C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
                cursor = cnxn.cursor()
                cursor.execte("DELETE FROM Listens WHERE ListenID = ?", self.ui.listenidbox.text())
                self.close()
                load = editlistens.editlistens(self)
                load.show()
            except:
                QtGui.QMessageBox.about(self, 'Error', 'An error has occured')
        elif ret == QtGui.QMessageBox.No:
            QtGui.QMessageBox.about(self, 'OK', 'Listen not deleted')