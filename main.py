
########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
import PySide2 
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from DRONE import Ui_MainWindow
from qt_material import*

########################################################################
# IMPORT GUI FILE
import ui_DRONE
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################



########################################################################
## MAIN WINDOW CLASS
########################################################################
#class MyApp(QtGui.QMainWindow, clientGUI.Ui_MainWindow):
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_cyan.xml')

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        apply_stylesheet(app, theme='dark_cyan.xml')

        ########################################################################
        set
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 
        self.setWindowFlags(QtCore.Qt.Rrame)





########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  

