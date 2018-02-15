import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from startwindow import StartWindow

if __name__ == '__main__':

    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'Music Indexer' )

    # create widget
    w = StartWindow()
    w.setWindowTitle( 'Music Indexer' )
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
