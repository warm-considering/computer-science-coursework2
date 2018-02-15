from PyQt4 import uic, QtGui
import pickle
import edituser
import pyodbc
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
( Ui_edituserdetails, QDialog ) = uic.loadUiType( 'edituserdetails.ui' )
def populate(self):
    searchterm = pickle.load(open("searchterm.temp", "rb"))
    print(str(searchterm))
    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
    cursor = cnxn.cursor()
    try:
        cursor.execute("SELECT * FROM Users WHERE UserID = ?",int(searchterm))
    except:
        cursor.execute("SELECT * FROM Users WHERE Username = ?",str(searchterm))
    row = cursor.fetchone()
    cnxn.close()
    self.ui.useridbox.setText(str(row[0]))
    self.ui.usernamebox_2.setText(str(row[1]))
    try:
        decryptionkey = pickle.load(open("DCKTMP", "rb"))
        encoded_key = open("privatekey.bin", "rb").read()
        privatekey = RSA.import_key(encoded_key, passphrase=decryptionkey)
        cipherRSA = PKCS1_OAEP.new(privatekey)
        newrow2 = cipherRSA.decrypt(row[2])
        newrow2 = newrow2.decode('utf-8')
        self.ui.passwordbox.setText(newrow2)
    except:
        self.ui.passwordbox.setText("Decryption key incorrect")
        self.ui.confirmbutton.setEnabled(False)
    self.ui.usersincebox.setText(str(row[3]))
class edituserdetails ( QDialog ):
    """edituserdetails inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_edituserdetails()
        self.ui.setupUi( self )
        populate(self)

    def __del__ ( self ):
        self.ui = None
    def confirm(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
        try:
            cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
            cursor = cnxn.cursor()
            cursor.execute("UPDATE Users SET Username = ? WHERE UserID = ?",self.ui.usernamebox_2.text(),self.ui.useridbox.text())
            publickey = RSA.import_key(open("publickey.bin", "rb").read())
            cipherRSA = PKCS1_OAEP.new(publickey)
            encryptedpassword = cipherRSA.encrypt(bytes(self.ui.passwordbox.text(), 'utf-8'))
            cursor.execute("UPDATE Users SET PasswordEncrypted = ? WHERE UserID = ?", encryptedpassword , self.ui.useridbox.text())
            cursor.execute("UPDATE Users SET UserSince = ? WHERE UserID = ?",self.ui.usersincebox.text(),self.ui.useridbox.text())
            h = SHA256.new()
            h.update(bytes(self.ui.passwordbox.text(), 'utf-8'))
            cursor.execute("UPDATE Users SET Hash = ? WHERE UserID = ?",h.digest(),self.ui.useridbox.text())
            cnxn.commit()
            cnxn.close()
            QtGui.QMessageBox.about(self, 'Success', 'The data has been changed')
        except:
            QtGui.QMessageBox.about(self, 'Error', 'An Error has Occured')
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = edituser.edituser(self)
        load.show()
