from PyQt4 import uic
import login
import register
( Ui_StartWindow, QMainWindow ) = uic.loadUiType( 'startwindow.ui' )

class StartWindow ( QMainWindow ):
    """StartWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_StartWindow()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def login(self):
        self.close()
        self.load = login.login()
        self.load.exec_()
        
    def register(self):
        
        load = register.register(self)
        load.show()
        self.close()
        