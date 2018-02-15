from PyQt4 import uic, QtGui
import pyodbc
import mainwindow
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
import datetime
import pickle
( Ui_register, QMainWindow ) = uic.loadUiType( 'register.ui' )

class register ( QMainWindow ):
    """register inherits QDialog"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_register()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def login(self):
        print("remember to fix this")
        if self.ui.password.text() == self.ui.confirmpassword.text():
            cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
            cursor = cnxn.cursor()
            publickey = RSA.import_key(open("publickey.bin", "rb").read())
            cipherRSA = PKCS1_OAEP.new(publickey)
            encryptedpassword = cipherRSA.encrypt(bytes(self.ui.password.text(), 'utf-8'))
            h = SHA256.new()
            h.update(bytes(self.ui.password.text(), 'utf-8'))
            cursor.execute("INSERT INTO Users (Username, PasswordEncrypted, UserSince, Hash) VALUES (?, ?, ?, ?)", self.ui.username.text(), encryptedpassword, datetime.datetime.now().strftime("%d-%m-%Y"), h.digest())
            cursor.execute("SELECT * FROM Users WHERE Username = ? AND Hash = ?", self.ui.username.text(), h.digest())
            userinfo = cursor.fetchone()
            userid = userinfo[0]
            pickle.dump( [3], open( str(userid)+"queue.db", "wb"))
            cnxn.commit()
            cnxn.close()
            pickle.dump( self.ui.username.text(), open("USRTMP", "wb"))
            pickle.dump( self.ui.password.text(), open("URPTMP", "wb"))
            
            self.close()
            self.load = mainwindow.mainwindow()
            self.load.exec_()
        else:
            print("well done")