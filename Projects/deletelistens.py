from PyQt4 import uic
import listendetails
( Ui_deletelistens, QDialog ) = uic.loadUiType( 'deletelistens.ui' )

class deletelistens ( QDialog ):
    """deletelistens inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_deletelistens()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def delete(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        print("fix this")
    def back(self):
        sentby = self.sender()
        print("sent by "+sentby.objectName())
        self.close()
        load = listendetails.listendetails(self)
        load.show()