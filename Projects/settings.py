from PyQt4 import uic
import userdecrypt
import songdetails
import listendetails
import advancedsettings
( Ui_settings, QDialog ) = uic.loadUiType( 'settings.ui' )

class settings ( QDialog ):
    """settings inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_settings()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def userdetails(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = userdecrypt.userdecrypt(self)
        load.show()
    def songdetails(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = songdetails.songdetails(self)
        load.show()
    def listendetails(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = listendetails.listendetails(self)
        load.show()
    def advanced(self):
        load = advancedsettings.advancedsettings(self)
        load.show()
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()