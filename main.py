import os, sys
from ui import Ui_RocketDesigner
from about_ui import Ui_AboutForm 
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
    ui_about.logo_label.setPixmap(QPixmap(os.path.join(path, './image/logo.jpg')))

def setupMenu(ui, AboutForm):
    ui.actionAbout.triggered.connect(lambda: AboutForm.show())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Init Main Window UI
    RocketDesigner = QMainWindow()
    ui = Ui_RocketDesigner()
    ui.setupUi(RocketDesigner)

    # Show menubar on main window
    menu = ui.menuBar
    menu.setNativeMenuBar(False)

    #Init About Form UI
    ui_about = Ui_AboutForm()
    AboutForm = QWidget()
    ui_about.setupUi(AboutForm)
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
    setupMenu(ui, AboutForm)

    RocketDesigner.show()    
    sys.exit(app.exec_())
