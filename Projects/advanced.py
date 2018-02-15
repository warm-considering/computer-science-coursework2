from PyQt4 import uic

(Ui_advanced, QMainWindow) = uic.loadUiType('advanced.ui')

class advanced (QMainWindow):
    """advanced inherits QMainWindow"""

    def __init__ (self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_advanced()
        self.ui.setupUi(self)

    def __del__ (self):
        self.ui = None
