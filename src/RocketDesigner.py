import os, sys
from ui import Ui_RocketDesigner
from about_ui import Ui_AboutForm 
from cs_ui import Ui_cs_form 
from example_ui import Ui_expForm
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout, QShortcut, QMainWindow)
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator, QKeySequence, QPixmap
from PyQt5.QtGui import QIcon
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
import math
import config
import mission, thermochemical, nozzle, chamber, feed, injector, ignitor, grain
import example
import cheatsheet 
import qdarktheme
import pdb

def runButtonEvent(ui):
    AllRun(ui)
    # tabIndex = ui.tabWidget.currentIndex()
    # if tabIndex == 0:
    #     mission.run(ui)
    # elif tabIndex == 1:
    #     thermochemical.run(ui)
    # elif tabIndex == 2:
    #     nozzle.run(ui)
    # elif tabIndex == 3:
    #     chamber.run(ui)
    # elif tabIndex == 4:
    #     feed.run(ui)
    # elif tabIndex == 5:
    #     pass
    # elif tabIndex == 6:
    #     pass

def AllRun(ui):
    mission.run(ui)
    UpdateThermoVariables(ui)
    thermochemical.run(ui)
    UpdateNozzleVariables(ui)
    nozzle.run(ui)
    UpdateChamberVariables(ui)
    chamber.run(ui)
    UpdateFeedVariables(ui)
    feed.run(ui)
    UpdateIgnitorVariables(ui)
    ignitor.run(ui)
    UpdateInjectorVariables(ui)
    injector.run(ui)
    UpdateGrainVariables(ui)
    grain.run(ui)

def UpdateThermoVariables(ui):
    pass

def UpdateNozzleVariables(ui):
    ui.le_pc_2.setText(ui.le_pc.text())
    ui.le_aft_2.setText(ui.le_aft.text())
    ui.le_gamma_2.setText(ui.le_gamma.text())
    ui.le_mdot_2.setText(ui.le_mdot.text())
    ui.le_M_2.setText(ui.le_M.text())      

def UpdateChamberVariables(ui):
    ui.le_at_2.setText(ui.le_at.text())

def UpdateFeedVariables(ui):
    pass
def UpdateIgnitorVariables(ui):
    pass
def UpdateInjectorVariables(ui):
    pass
def UpdateGrainVariables(ui):
    pass

def quitEvent(window):
    window.close()

def setupShortcut(ui, MainWindow, ui_cs, cs_form):
    shortcutRun = QKeySequence(Qt.CTRL + Qt.Key_R)
    shortcutQuit = QKeySequence(Qt.CTRL + Qt.Key_W)
    shortcutCS = QKeySequence(Qt.CTRL + Qt.Key_I)

    ui.shortcut = QShortcut(shortcutRun, ui.tabWidget)
    ui.shortcut2 = QShortcut(shortcutQuit, ui.tabWidget)
    ui.shortcut3 = QShortcut(shortcutCS, ui.tabWidget)
    ui_cs.shortcut4 = QShortcut(shortcutQuit, ui_cs.webViewWidget)

    ui.shortcut.activated.connect(lambda: runButtonEvent(ui))
    ui.shortcut2.activated.connect(lambda: quitEvent(MainWindow))
    ui.shortcut3.activated.connect(lambda: cheatsheet.show(ui, ui_cs, cs_form))
    ui_cs.shortcut4.activated.connect(lambda: quitEvent(cs_form))

def loadImages(ui_about):
    path = os.path.dirname(os.path.abspath(__file__))
    ui_about.logo_label.setPixmap(QPixmap(os.path.join(path, './image/logo_100px.png')))

def setupMenu(ui, ui_cs, AboutForm, expForm, cs_form):
    ui.actionAbout.triggered.connect(lambda: AboutForm.show())
    ui.actionRun.triggered.connect(lambda: AllRun(ui))
    ui.actionExamples.triggered.connect(lambda: expForm.show())
    ui.actionCheatsheet.triggered.connect(lambda: cheatsheet.show(ui, ui_cs, cs_form))

def setupHandlers(ui):
    ui.tabWidget.currentChanged.connect(lambda: tabSwitchedEvent(ui))

def tabSwitchedEvent(ui):
    # print(ui.tabWidget.currentIndex())
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = os.path.dirname(os.path.abspath(__file__))
    icon = QIcon(os.path.join(path, './image/logo_100px.png'))
    app.setWindowIcon(icon) 
    qdarktheme.setup_theme("light")

    #Init Main Window UI
    RocketDesigner = QMainWindow()
    ui = Ui_RocketDesigner()
    ui.setupUi(RocketDesigner)

    # Show menubar on main window
    menu = ui.menuBar
    menu.setNativeMenuBar(False)

    #Init About UI
    ui_about = Ui_AboutForm()
    AboutForm = QWidget()
    ui_about.setupUi(AboutForm)
    loadImages(ui_about)

    #Init Cheatsheet Mission UI
    cs_form = QWidget()
    ui_cs = Ui_cs_form()
    ui_cs.setupUi(cs_form)
    cheatsheet.initialize(ui, ui_cs, cs_form)

    #Init example UI
    expForm = QWidget()
    ui_exp = Ui_expForm()
    ui_exp.setupUi(expForm)
    example.initialize(ui, ui_exp)

    mission.initialize(ui) 
    thermochemical.initialize(ui)
    nozzle.initialize(ui)
    chamber.initialize(ui)
    feed.initialize(ui)
    ignitor.initialize(ui)
    injector.initialize(ui)
    grain.initialize(ui)

    setupHandlers(ui)
    setupShortcut(ui, RocketDesigner, ui_cs, cs_form)
    setupMenu(ui, ui_cs, AboutForm, expForm, cs_form)

    RocketDesigner.show()    
    sys.exit(app.exec_())
