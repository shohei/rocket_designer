import sys
from ui import Ui_Form
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout)
from PyQt5.QtCore import Qt
import math

g = 9.8 #m/s^2

def calculate(ui):
    print("calculate")
    h = float(ui.le_apogee.text())
    deltaV = math.sqrt(2*g*h)
    
    I = m0*deltaV 
    MR = 
    ui.le_deltav.setText(deltaV)
    ui.le_impulse.setText(I)
    ui.le_mr.setText(MR)

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

