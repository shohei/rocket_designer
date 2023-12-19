import os, sys
from ui import Ui_MainWindow
from about_ui import Ui_Form as Ui_About
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout, QShortcut, QMainWindow)
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator, QKeySequence, QPixmap
import math
import config
from components import mission, thermochemical, nozzle, chamber, feed, injector, ignitor, grain
import pdb

def runButtonEvent(ui):
    print('run')
    tabIndex = ui.tabWidget.currentIndex()
    if tabIndex == 0:
        mission.run(ui)
    elif tabIndex == 1:
        pass
    elif tabIndex == 2:
        pass
    elif tabIndex == 3:
        pass
    elif tabIndex == 4:
        pass

def setupShortcut(ui):
    shortcut = QKeySequence(Qt.CTRL + Qt.Key_R)
    ui.shortcut = QShortcut(shortcut, ui.tabWidget)
    ui.shortcut.activated.connect(lambda: runButtonEvent(ui))

def loadImages(ui_about):
    path = os.path.dirname(os.path.abspath(__file__))
    ui_about.logo_label.setPixmap(QPixmap(os.path.join(path, '../image/logo.jpg')))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Init Main Window UI
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # menu = ui.menubar
    # menu.setNativeMenuBar(False)

    #Init About Form UI
    ui_about = Ui_About()
    aboutForm = QWidget()
    ui_about.setupUi(aboutForm)
    loadImages(ui_about)

    mission.initialize(ui) 
    thermochemical.initialize(ui)
    nozzle.initialize(ui)
    chamber.initialize(ui)
    feed.initialize(ui)
    ignitor.initialize(ui)
    injector.initialize(ui)
    grain.initialize(ui)
    setupShortcut(ui)

    MainWindow.show()
    sys.exit(app.exec_())
