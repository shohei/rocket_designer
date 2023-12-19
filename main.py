import sys
from ui import Ui_Form
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout)
from PyQt5.QtCore import Qt
import math

g = 9.8 #m/s^2

def calculate(ui):
    print("calculate")
    h = ui.le_apogee.text()
    if h=='':
        h = 2.0
        ui.le_apogee.setText(str(h))
    else:
        h = float(h)
    m0 = ui.le_m0.text()
    if m0=='':
        m0 = 10.0
        ui.le_m0.setText(str(m0))
    else:
        m0 = float(m0)
    Isp = ui.le_isp.text()
    if Isp=='':
        Isp = 110
        ui.le_isp.setText(str(Isp))
    else:
        Isp = float(Isp)

    deltaV = math.sqrt(2*g*h)
    I = m0*deltaV 
    MR = math.exp(deltaV/g*Isp)
    ui.le_deltav.setText(str(deltaV).format("%.2g"))
    ui.le_impulse.setText(str(I).format("%.2g"))
    ui.le_mr.setText(str(MR).format("%.2g"))

def setupHandlers(ui):
    ui.pushButton.clicked.connect(lambda: calculate(ui))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    setupHandlers(ui)
    Form.show()
    sys.exit(app.exec_())

