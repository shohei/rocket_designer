import os, sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout, QShortcut)
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator, QKeySequence, QPixmap
import math
import config
from components import *

def run(ui):
    g = config.g
    h = float(ui.le_apogee.text())
    m0 = float(ui.le_m0.text())
    Isp = float(ui.le_isp.text())
    burntime = float(ui.le_burntime.text())

    deltaV = math.sqrt(2*g*h)
    I = m0*deltaV 
    MR = math.exp(deltaV/(g*Isp))
    mp= (MR-1)/MR*m0
    avg_thrust = I/burntime
    ui.le_deltav.setText("{:.2f}".format((deltaV)))
    ui.le_impulse.setText("{:.2f}".format((I)))
    ui.le_mr.setText("{:.2f}".format((MR)))
    ui.le_thrust.setText("{:.2f}".format((avg_thrust)))
    ui.le_mp.setText("{:.2f}".format((mp)))

def setupHandlers(ui):
    ui.runMissionButton.clicked.connect(lambda: run(ui))
    ui.tabWidget.currentChanged.connect(lambda: tabSwitchedEvent(ui))

def tabSwitchedEvent(ui):
    print(ui.tabWidget.currentIndex())

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

def initializeN3parameters(ui):
    ui.le_apogee.setText('2000.0')
    ui.le_isp.setText('110.0')
    ui.le_m0.setText('10.0')
    ui.le_burntime.setText('1.8')

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
    loadImages(ui)
    initializeN3parameters(ui)