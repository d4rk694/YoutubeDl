#!/user/bin/env python3 -tt
# Imports
import sys
from window import *
from PyQt5 import QtGui, QtCore, QtWidgets, sip


# Cmd C:\Users\gaetb\AppData\Local\Programs\Python\Python36-32\Scripts\pyuic5.exe -x .\mainwindow.ui -o test.py
# Global variables

PLAYLIST_NAME = "https://www.youtube.com/playlist?list=PL-PHOurQ0Fdj8uFTqOQ51rk-6ae49N-Uz"
LIMIT_NAME_SIZE = 60
LIMIT_AUTHOR_SIZE = 40
PLAYLIST_ENTRY_DEFAULT = "Entrez le lien de votre playlist"
class Window(object):

    # Front end Functions
    def launchFront(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


    def main(self):
        import os

        self.launchFront()
        #self.second()
        #launchBack()
if __name__ == '__main__':
    Window().main()
