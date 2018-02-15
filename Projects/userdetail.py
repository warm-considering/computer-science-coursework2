from PyQt4 import uic, QtGui
import userdecrypt
import edituser
import pyodbc
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
( Ui_userdetail, QDialog ) = uic.loadUiType( 'userdetail.ui' )

class userdetail ( QDialog ):
    """userdetail inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_userdetail()
        self.ui.setupUi( self )

    def populate(self):
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Users")
        row = cursor.fetchall()
        cnxn.close()
        for item in row:
            rowcount = self.ui.usertable.rowCount()
            self.ui.usertable.insertRow(rowcount)
            self.ui.usertable.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
            self.ui.usertable.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
            try:
                decryptionkey = pickle.load(open("DCKTMP", "rb"))
                encoded_key = open("privatekey.bin", "rb").read()
                privatekey = RSA.import_key(encoded_key, passphrase=decryptionkey)
                cipherRSA = PKCS1_OAEP.new(privatekey)
                newitem2 = cipherRSA.decrypt(item[2])
                newitem2 = newitem2.decode('utf-8')
                self.ui.usertable.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(newitem2)))
            except:
                self.ui.usertable.setItem(rowcount, 2,QtGui.QTableWidgetItem("Decryption key incorrect"))
            self.ui.usertable.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
    def __del__ ( self ):
        self.ui = None
    def edit(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = edituser.edituser(self)
        load.show()
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = userdecrypt.userdecrypt(self)
        load.show()