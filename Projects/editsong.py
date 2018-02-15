from PyQt4 import uic
import songdetails
( Ui_editsong, QDialog ) = uic.loadUiType( 'editsong.ui' )

class editsong ( QDialog ):
    """editsong inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_editsong()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def refresh(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    def delete(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        load = songdetails.songdetails(self)
        load.show()
