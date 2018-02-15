from PyQt4 import uic, QtCore, QtGui
import pyodbc
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

(Ui_advancedsettings, QDialog) = uic.loadUiType('advancedsettings.ui')

class advancedsettings (QDialog):
    """advancedsettings inherits QDialog"""

    def __init__ (self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_advancedsettings()
        self.ui.setupUi(self)
        for i in range(1,21):
            getattr(self.ui, "line"+str(i)).setDisabled(True)
        for i in range(2,22):
            getattr(self.ui, "label_"+str(i)).setText("")
        options = ["Users", "Songs", "Listens"]
        self.ui.dropdownbox.addItems(options)
        

    def __del__ (self):
        self.ui = None
    
    def tablechanged(self):
        if self.ui.dropdownbox.currentText() == "Users":
            self.ui.tablewidget.setRowCount(0)
            self.ui.label_2.setText("UserID")
            self.ui.label_3.setText("Username")
            self.ui.label_4.setText("Password")
            self.ui.label_5.setText("UserSince")
            self.ui.label_6.setText("Hash")
            for i in range(7,22):
                getattr(self.ui, "label_"+str(i)).setText("")
            for i in range(1,6):
                getattr(self.ui, "line"+str(i)).setDisabled(False)
            for i in range(6,21):
                getattr(self.ui, "line"+str(i)).setDisabled(True)
            self.ui.tablewidget.setColumnCount(5)
            headers = ["UserID", "Username", "Password", "UserSince", "Hash"]
            self.ui.tablewidget.setHorizontalHeaderLabels(headers)
        if self.ui.dropdownbox.currentText() == "Songs":
            self.ui.tablewidget.setRowCount(0)
            self.ui.label_2.setText("SongID")
            self.ui.label_3.setText("VideoName")
            self.ui.label_4.setText("VideoID")
            self.ui.label_5.setText("VideoViews")
            self.ui.label_6.setText("Likes")
            self.ui.label_7.setText("Dislikes")
            self.ui.label_8.setText("Artist")
            self.ui.label_9.setText("Title")
            self.ui.label_10.setText("Album")
            self.ui.label_11.setText("Genre")
            self.ui.label_12.setText("Related1")
            self.ui.label_13.setText("Related2")
            self.ui.label_14.setText("Related3")
            self.ui.label_15.setText("Related4")
            self.ui.label_16.setText("Related5")
            self.ui.label_17.setText("Related6")
            self.ui.label_18.setText("Related7")
            self.ui.label_19.setText("Related8")
            self.ui.label_20.setText("Related9")
            self.ui.label_21.setText("Related10")
            self.ui.tablewidget.setColumnCount(20)
            headers = ["SongID", "VideoName", "VideoID", "VideoViews", "Likes", "Dislikes", "Related1", "Related2", "Related3", "Related4", "Related5", "Related6", "Related7", "Related8", "Related9", "Related10", "Artist", "Title", "Album", "Genre"]
            self.ui.tablewidget.setHorizontalHeaderLabels(headers)
            for i in range(1,21):
                getattr(self.ui, "line"+str(i)).setDisabled(False)
        if self.ui.dropdownbox.currentText() == "Listens":
            self.ui.tablewidget.setRowCount(0)
            self.ui.label_2.setText("ListenID")
            self.ui.label_3.setText("SongID")
            self.ui.label_4.setText("UserID")
            self.ui.label_5.setText("NoOfListen")
            self.ui.label_6.setText("Rating")
            self.ui.label_7.setText("LastListen")
            self.ui.tablewidget.setColumnCount(6)
            headers = ["ListenID", "SongID", "UserID", "NoOfListen", "Rating", "LastListen"]
            self.ui.tablewidget.setHorizontalHeaderLabels(headers)
            for i in range(8,22):
                getattr(self.ui, "label_"+str(i)).setText("")
            for i in range(1,7):
                getattr(self.ui, "line"+str(i)).setDisabled(False)
            for i in range(7,21):
                getattr(self.ui, "line"+str(i)).setDisabled(True)
        
    
    def back(self):
        self.close()
    
    def fetch(self):
        if self.ui.dropdownbox.currentText() == "Users":
            self.ui.tablewidget.setRowCount(0)
            cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM Users")
            row = cursor.fetchall()
            cnxn.close()
            for item in row:
                rowcount = self.ui.tablewidget.rowCount()
                self.ui.tablewidget.insertRow(rowcount)
                self.ui.tablewidget.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
                self.ui.tablewidget.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
                try:
                    decryptionkey = self.ui.decryptionkey.text()
                    encoded_key = open("privatekey.bin", "rb").read()
                    privatekey = RSA.import_key(encoded_key, passphrase=decryptionkey)
                    cipherRSA = PKCS1_OAEP.new(privatekey)
                    newitem2 = cipherRSA.decrypt(item[2])
                    newitem2 = newitem2.decode('utf-8')
                    self.ui.tablewidget.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(newitem2)))
                except:
                    self.ui.tablewidget.setItem(rowcount, 2,QtGui.QTableWidgetItem("Decryption key incorrect"))
                self.ui.tablewidget.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
                self.ui.tablewidget.setItem(rowcount, 4,QtGui.QTableWidgetItem(str(item[4])))
        elif self.ui.dropdownbox.currentText() == "Songs":
                    self.ui.tablewidget.setRowCount(0)
                    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
                    cursor = cnxn.cursor()
                    cursor.execute("SELECT * FROM Songs")
                    row = cursor.fetchall()
                    cnxn.close()
                    for item in row:
                        rowcount = self.ui.tablewidget.rowCount()
                        self.ui.tablewidget.insertRow(rowcount)
                        self.ui.tablewidget.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
                        self.ui.tablewidget.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
                        self.ui.tablewidget.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(item[2])))
                        self.ui.tablewidget.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
                        self.ui.tablewidget.setItem(rowcount, 4,QtGui.QTableWidgetItem(str(item[4])))
                        self.ui.tablewidget.setItem(rowcount, 5,QtGui.QTableWidgetItem(str(item[5])))
                        self.ui.tablewidget.setItem(rowcount, 6,QtGui.QTableWidgetItem(str(item[6])))
                        self.ui.tablewidget.setItem(rowcount, 7,QtGui.QTableWidgetItem(str(item[7])))
                        self.ui.tablewidget.setItem(rowcount, 8,QtGui.QTableWidgetItem(str(item[8])))
                        self.ui.tablewidget.setItem(rowcount, 9,QtGui.QTableWidgetItem(str(item[9])))
                        self.ui.tablewidget.setItem(rowcount, 10,QtGui.QTableWidgetItem(str(item[10])))
                        self.ui.tablewidget.setItem(rowcount, 11,QtGui.QTableWidgetItem(str(item[11])))
                        self.ui.tablewidget.setItem(rowcount, 12,QtGui.QTableWidgetItem(str(item[12])))
                        self.ui.tablewidget.setItem(rowcount, 13,QtGui.QTableWidgetItem(str(item[13])))
                        self.ui.tablewidget.setItem(rowcount, 14,QtGui.QTableWidgetItem(str(item[14])))
                        self.ui.tablewidget.setItem(rowcount, 15,QtGui.QTableWidgetItem(str(item[15])))
                        self.ui.tablewidget.setItem(rowcount, 16,QtGui.QTableWidgetItem(str(item[16])))
                        self.ui.tablewidget.setItem(rowcount, 17,QtGui.QTableWidgetItem(str(item[17])))
                        self.ui.tablewidget.setItem(rowcount, 18,QtGui.QTableWidgetItem(str(item[18])))
                        self.ui.tablewidget.setItem(rowcount, 19,QtGui.QTableWidgetItem(str(item[19])))
        elif self.ui.dropdownbox.currentText() == "Listens":
                    self.ui.tablewidget.setRowCount(0)
                    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
                    cursor = cnxn.cursor()
                    cursor.execute("SELECT * FROM Listens")
                    row = cursor.fetchall()
                    cnxn.close()
                    for item in row:
                        rowcount = self.ui.tablewidget.rowCount()
                        self.ui.tablewidget.insertRow(rowcount)
                        self.ui.tablewidget.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
                        self.ui.tablewidget.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
                        self.ui.tablewidget.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(item[2])))
                        self.ui.tablewidget.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
                        self.ui.tablewidget.setItem(rowcount, 4,QtGui.QTableWidgetItem(str(item[4])))
                        self.ui.tablewidget.setItem(rowcount, 5,QtGui.QTableWidgetItem(str(item[5])))
    
    def search(self):
        if self.ui.dropdownbox.currentText() == "Users":
            cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
            cursor = cnxn.cursor()
            try:
                int(self.ui.searchtext.text())
                cursor.execute("SELECT * FROM Users WHERE UserID = ?",self.ui.searchtext.text())
                all = cursor.fetchall()
            except:
                cursor.execute("SELECT * FROM Users WHERE Username = ?",self.ui.searchtext.text())
                all = cursor.fetchall()
            if len(all) == 1:
                row = all[0]
                cnxn.close()
                self.ui.line1.setText(str(row[0]))
                self.ui.line2.setText(str(row[1]))
                try:
                    decryptionkey = self.ui.decryptionkey.text()
                    encoded_key = open("privatekey.bin", "rb").read()
                    privatekey = RSA.import_key(encoded_key, passphrase=decryptionkey)
                    cipherRSA = PKCS1_OAEP.new(privatekey)
                    newrow2 = cipherRSA.decrypt(row[2])
                    newrow2 = newrow2.decode('utf-8')
                    self.ui.line3.setText(newrow2)
                except:
                    self.ui.line3.setText("Decryption key incorrect")
                self.ui.line4.setText(str(row[3]))
                self.ui.line5.setText(str(row[4]))
            else:
                row = all
                cnxn.close()
                for i in range(1,21):
                    getattr(self.ui, "line"+str(i)).setText("")
                for item in row:
                    rowcount = self.ui.tablewidget.rowCount()
                    self.ui.tablewidget.insertRow(rowcount)
                    self.ui.tablewidget.setItem(rowcount, 0,QtGui.QTableWidgetItem(str(item[0])))
                    self.ui.tablewidget.setItem(rowcount, 1,QtGui.QTableWidgetItem(str(item[1])))
                    try:
                        decryptionkey = self.ui.decryptionkey.text()
                        encoded_key = open("privatekey.bin", "rb").read()
                        privatekey = RSA.import_key(encoded_key, passphrase=decryptionkey)
                        cipherRSA = PKCS1_OAEP.new(privatekey)
                        newitem2 = cipherRSA.decrypt(item[2])
                        newitem2 = newitem2.decode('utf-8')
                        self.ui.tablewidget.setItem(rowcount, 2,QtGui.QTableWidgetItem(str(newitem2)))
                    except:
                        self.ui.tablewidget.setItem(rowcount, 2,QtGui.QTableWidgetItem("Decryption key incorrect"))
                    self.ui.tablewidget.setItem(rowcount, 3,QtGui.QTableWidgetItem(str(item[3])))
                    self.ui.tablewidget.setItem(rowcount, 4,QtGui.QTableWidgetItem(str(item[4])))
        if self.ui.dropdownbox.currentText() == "Songs":
            cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
            cursor = cnxn.cursor()
            try:
                int(self.ui.searchtext.text())
                cursor.execute("SELECT * FROM Songs WHERE SongID = ?",self.ui.searchtext.text())
                all = cursor.fetchall()
            except:
                cursor.execute("SELECT * FROM Songs WHERE VideoName = ?",self.ui.searchtext.text())
                all = cursor.fetchall()
            if len(all) == 1:
                row = all[0]
                cnxn.close()
                for i in range(1, 21):
                    getattr(self.ui, "line"+str(i)).setText(str(row[i-1]))
    
    def updatetable(self):
        pass
    
    def delete(self):
        pass
    
    def add(self):
        pass

    def tableclicked(self):
        pass
