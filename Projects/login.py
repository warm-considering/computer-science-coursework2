from PyQt4 import uic
import mainwindow
( Ui_login, QMainWindow ) = uic.loadUiType( 'login.ui' )
userid=0
class login ( QMainWindow ):
    """login inherits QDialog"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_login()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    def login(self):
        print("remember to fix this")
        
        #pickle.dump( self.ui.username.text(), open("USRTMP", "wb"))
        #pickle.dump( self.ui.password.text(), open("URPTMP", "wb"))
        self.close()
        self.load = mainwindow.mainwindow()
        self.load.exec_()
