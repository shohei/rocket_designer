import os
import math
from PyQt5.QtGui import QRegExpValidator, QKeySequence, QPixmap

def run(ui):
    Lstar = float(ui.le_lstar.text())# [cm] characteristic length
    At = float(ui.le_at_2.text())*1e-2 # [cm^2] throat area
    Vc = Lstar*At # [cm^3] chamber volume
    Dt = math.sqrt(4*At/math.pi) #[cm]
    Ac = 8.0*Dt**(-0.8)+1.25 #[cm^2]
    Dc = 2*math.sqrt(Ac/math.pi) #[cm]
    Lc = Vc/Ac #[cm]
    ui.le_vc.setText("{:.2f}".format((Vc))) # [cm^3] chamber volume
    ui.le_dc.setText("{:.2f}".format((Dc*1e1))) # [mm] chamber volume
    ui.le_lc.setText("{:.2f}".format((Lc))) # [cm] chamber volume

def initVariables(ui):
    ui.le_lstar.setText('100.0')
    ui.le_at_2.setText(ui.le_at.text())

def loadImages(ui):
    path = os.path.dirname(os.path.abspath(__file__))
    ui.lbl_lstar.setPixmap(QPixmap(os.path.join(path, './image/Lstar.png')))

def initHandlers(ui):
    ui.runChamberButton.clicked.connect(lambda: run(ui))

def initialize(ui):
    loadImages(ui)
    initHandlers(ui)
    initVariables(ui)
    run(ui)
