import os, sys
from ui import Ui_Form
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout, QShortcut)
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator, QKeySequence, QPixmap
import math
import config
from components import mission, thermochemical, nozzle, chamber, feed, injector, ignitor

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    mission.initialize(ui) 
    setupShortcut(ui)
    Form.show()
    sys.exit(app.exec_())
