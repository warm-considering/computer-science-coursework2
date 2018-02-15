from PyQt4 import uic
import pickle
import userdetail
import settings
( Ui_userdecrypt, QDialog ) = uic.loadUiType( 'userdecrypt.ui' )

class userdecrypt ( QDialog ):
    """userdecrypt inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_userdecrypt()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def view(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix me")
        pickle.dump( self.ui.decryptionkey.text(), open("DCKTMP", "wb"))
        self.close()
        load = userdetail.userdetail(self)
        load.show()
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = settings.settings(self)
        load.show()
