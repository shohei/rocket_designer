import os, sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout, QShortcut)
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator, QKeySequence, QPixmap
import math
import config

def run(ui):
    g = config.g
    h = float(ui.le_apogee.text())*1000
    m0 = float(ui.le_m0.text())
    Isp = float(ui.le_isp.text())
    burntime = float(ui.le_burntime.text())

    deltaV = math.sqrt(2*g*h)
    I = m0*deltaV
    MR = math.exp(deltaV/(g*Isp))
    mp= (MR-1)/MR*m0
    avg_thrust = I/burntime
    mass_flow_rate = mp/burntime
    ui.le_deltav.setText("{:.2f}".format((deltaV)))
    ui.le_impulse.setText("{:.2f}".format((I/1000.0)))
    ui.le_mr.setText("{:.2f}".format((MR)))
    ui.le_thrust.setText("{:.2f}".format((avg_thrust/1000.0)))
    ui.le_mp.setText("{:.2f}".format((mp)))
    ui.le_mdot.setText("{:.2f}".format((mass_flow_rate)))

def setupHandlers(ui):
    ui.nakuja_n3_button.clicked.connect(lambda: initializeNakujaN3parameters(ui))
    ui.usc_traveler4_button.clicked.connect(lambda: initializeUSCTraveler4parameters(ui))
    ui.jaxa_ss520_button.clicked.connect(lambda: initializeJAXASS520parameters(ui))
    ui.nakuja_liquid1_button.clicked.connect(lambda: initializeNakujaLiquid1parameters(ui))
    ui.jaxa_h3_button.clicked.connect(lambda: initializeJAXAH3parameters(ui))
    ui.spacex_falcon9_button.clicked.connect(lambda: initializeSpaceXFalcon9parameters(ui))
    ui.tabWidget.currentChanged.connect(lambda: tabSwitchedEvent(ui))

def tabSwitchedEvent(ui):
    # print(ui.tabWidget.currentIndex())
    pass

def setupValidators(ui):
    validator = QRegExpValidator(QRegExp(r'[0-9].+'))
    ui.le_apogee.setValidator(validator)
    ui.le_isp.setValidator(validator)
    ui.le_m0.setValidator(validator)
    ui.le_deltav.setValidator(validator)
    ui.le_impulse.setValidator(validator)
    ui.le_mr.setValidator(validator)
    ui.le_mr.setValidator(validator)
    ui.le_thrust.setValidator(validator)
    ui.le_thrust.setValidator(validator)
    ui.le_mp.setValidator(validator)

def initializeNakujaN3parameters(ui):
    ui.le_apogee.setText('2.0')
    ui.le_isp.setText('110.0')
    ui.le_m0.setText('10.0')
    ui.le_burntime.setText('1.8')

def initializeUSCTraveler4parameters(ui):
    ui.le_apogee.setText('103.5714')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def initializeJAXASS520parameters(ui):
    ui.le_apogee.setText('800.0')
    ui.le_isp.setText('282.6')
    ui.le_m0.setText('2740.0')
    ui.le_burntime.setText('25.6')

def initializeNakujaLiquid1parameters(ui):
    ui.le_apogee.setText('N/A')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def initializeJAXAH3parameters(ui):
    ui.le_apogee.setText('N/A')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def initializeSpaceXFalcon9parameters(ui):
    ui.le_apogee.setText('N/A')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

# ### Use this function To attach files to the exe file (eg - png, txt, jpg etc) using pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def loadImages(ui):
    path = os.path.dirname(os.path.abspath(__file__))
    ui.label.setPixmap(QPixmap(os.path.join(path, '../image/h3.jpg')))

def initialize(ui):
    setupHandlers(ui)
    setupValidators(ui)
    # loadImages(ui)
    initializeNakujaN3parameters(ui)
    run(ui)