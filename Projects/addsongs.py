from PyQt4 import uic
import songdetails
( Ui_addsongs, QDialog ) = uic.loadUiType( 'addsongs.ui' )

class addsongs ( QDialog ):
    """addsongs inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_addsongs()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def add(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
        
    def rescan(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = songdetails.songdetails(self)
        load.show()