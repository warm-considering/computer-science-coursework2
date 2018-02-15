from PyQt4 import uic, QtGui
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
import settings
import pickle
import pyodbc
import threading
import random
import pyglet
import pafy
from time import gmtime, strftime
import datetime
( Ui_mainwindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

def populatequeue(self, userid):
    queue = pickle.load(open(str(userid)+"queue.db", "rb"))
    for i in range(17):
        getattr(self.ui, "song"+str(i)).setText("")
    for i in range(17):
        try:
            getattr(self.ui, "song"+str(i)).setText(str(queue[i]))
        except:
            break



def populatebuttons(self, userid):
    queue = pickle.load(open(str(userid)+"queue.db", "rb"))
    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Songs WHERE SongID = ?", queue[0])
    newsong = cursor.fetchone()[1]
    self.ui.button1.setText(newsong)
    self.ui.button2.setText("Your Favourites")
    self.ui.button3.setText("Random Mix")
    for i in range(4,13):
        newsong = generaterandomsong(userid)
        print(newsong)
        if newsong == None:
            break
        cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * FROM Songs WHERE SongID = ?", newsong)
        newsong = cursor.fetchone()[1]
        getattr(self.ui, "button"+str(i)).setText(str(newsong))


def generaterandomsong(userid):
    print(userid)
    old = random.randint(1, 15)
    if old != 1:
        old = 0
    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
    cursor = cnxn.cursor()
    chosen = False
    cursor.execute("SELECT * FROM Listens WHERE UserID = ?", userid)
    if cursor.fetchall() == None:
        print("yep")
        return None
    if old == 0:
        cursor.execute("SELECT * FROM Listens WHERE UserID = ? AND LastListen < ?", userid, (datetime.datetime.now()-datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"))
        options = cursor.fetchall()
        if options == None:
            cursor.execute("SELECT * FROM Listens WHERE UserID = ? AND LastListen < ?", userid, (datetime.datetime.now()-datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S"))
            options = cursor.fetchall()
            if options == None:
                cursor.execute("SELECT * FROM Listens WHERE UserID = ? AND LastListen < ?", userid, (datetime.datetime.now()-datetime.timedelta(days=90)).strftime("%Y-%m-%d %H:%M:%S"))
                options = cursor.fetchall()
                if options == None:
                    old = 1
                else:
                    while chosen == False:
                        try:
                            selection = options[random.randint(0, (len(options)-1))]
                            if random.randint(1, 10) <= selection[4]:
                                chosen = True
                                return selection[1]
                        except:
                            selection = options[0]
                            return selection[1]
            else:
                while chosen == False:
                    try:
                        selection = options[random.randint(0, (len(options)-1))]
                        if random.randint(1, 10) <= selection[4]:
                            chosen = True
                            return selection[1]
                    except:
                        selection = options[0]
                        return selection[1]
        else:
            while chosen == False:
                try:
                    selection = options[random.randint(0, (len(options)-1))]
                    if random.randint(1, 10) <= selection[4]:
                        chosen = True
                        return selection[1]
                except:
                    selection = options[0]
                    return selection[1]
            
    if old == 1:
        cursor.execute("SELECT * FROM Listens WHERE UserID = ?", userid)
        options = cursor.fetchall()
        while chosen == False:
            try:
                selection = options[random.randint(0, (len(options)-1))]
                if random.randint(1, 10) <= selection[4]:
                    chosen = True
                    return selection[1]
            except:
                selection = options[0]
                return selection[1]

def backuprandomvideos():
    return "daisuki"



def userloggedin(self):
    return 56
    username = pickle.load( open("USRTMP", "rb"))
    password = pickle.load( open("URPTMP", "rb"))
    h = SHA256.new()
    h.update(bytes(password, 'utf-8'))
    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Hash = ?", username, h.digest())
    row = cursor.fetchone()
    cnxn.close()
    userid = row[0]
    print(userid)
    return userid
    
def playshiawase(self):
    global player
    player = pyglet.media.Player()
    songobject = pyglet.media.load("C:\\Users\\Home\\Music\\Shiawase Hiyori k-on (128kbit_AAC).mp3")
    pickle.dump(songobject.duration, open("SNGTMP", "wb"))
    player.queue(songobject)
    thread = threading.Thread(target=seekbar, args=(self, player, songobject.duration))
    thread.daemon = True
    thread.start()
    player.play()
    pyglet.app.run()
    duration = pickle.load(open("SNGTMP", "rb"))

    
    
def seekbar(self, player, duration):
    nowplaying = player.playing
    print(nowplaying)
    while True:
        newposition = round((player.time/duration)*1000)
        self.ui.horizontalSlider.setValue(newposition)

def play(self, button):
    global player
    player = pyglet.media.Player()
    cnxn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL=MS Access;DriverId=25;DefaultDir=C:\\Users\\sean\\Documents;DBQ=C:\\Users\\sean\\Documents\\Computer science coursework.mdb')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Songs WHERE VideoName = ?", button)
    song = cursor.fetchone()
    videoid = song[2]
    if len(videoid) == 11:
        myvid = pafy.new(videoid)
        playlist = myvid.mix
        stream = myvid.getbestaudio(preftype="m4a")
        songname = myvid.title.replace("/", "").replace(":", "").replace("\\", "").replace("*", "").replace("?","").replace('"', '').replace("<", "").replace(">","").replace("|","")
        try:
            stream.download("songs\\"+songname+'.m4a', quiet=True)
        except FileExistsError:
            pass
        songobject = pyglet.media.load("songs\\"+songname+'.m4a')
        pickle.dump(songobject.duration, open("SNGTMP", "wb"))
        player.queue(songobject)
        thread = threading.Thread(target=seekbar, args=(self, player, songobject.duration))
        thread.daemon = True
        thread.start()
        player.play()
        pyglet.app.run()
        duration = pickle.load(open("SNGTMP", "rb"))

    else:
        songobject = pyglet.media.load(videoid)
        pickle.dump(songobject.duration, open("SNGTMP", "wb"))
        player.queue(songobject)
        thread = threading.Thread(target=seekbar, args=(self, player, songobject.duration))
        thread.daemon = True
        thread.start()
        player.play()
        pyglet.app.run()
        duration = pickle.load(open("SNGTMP", "rb"))

class mainwindow ( QMainWindow ):
    """mainwindow inherits QDialog"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_mainwindow()
        self.ui.setupUi( self )
        userid = userloggedin(self)
        print(userid)
        populatequeue(self, userid)
        populatebuttons(self, userid)
        
    
    
    def __del__ ( self ):
        self.ui = None
    
    
    def search(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    
    
    def songbutton(self):
        sentby = self.sender()
        if  sentby.text() == "Shiawase Hiyori":
            playshiawase(self)
        else:
            play(self, sentby.text())
        print("sent by "+sentby.objectName())
        print("fix this")
    
    
    def rewind(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    
    
    def play(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
        global player
        if player.playing == True:
            player.pause()
        elif player.playing == False:
            player.play()
    

    def fastforward(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    
    
    def rate(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")

    
    
    def remove(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")

    
    
    def settings(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        load = settings.settings(self)
        load.show()
    
    def seek(self, int):
        duration = pickle.load(open("SNGTMP", "rb"))
        player.seek(((duration)/1000)*int)
