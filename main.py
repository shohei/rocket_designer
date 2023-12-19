import sys
from ui import Ui_Form
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout)
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.QtGui import QRegExpValidator
import math

g = 9.8 #m/s^2
validator = QRegExpValidator(QRegExp(r'[0-9].+'))

def calculate(ui):
    print("calculate")
    h = float(ui.le_apogee.text())
    m0 = float(ui.le_m0.text())
    Isp = float(ui.le_isp.text())
    burntime = float(ui.le_burntime.text())

    deltaV = math.sqrt(2*g*h)
    I = m0*deltaV 
    MR = math.exp(deltaV/(g*Isp))
    avg_thrust = I/burntime
    ui.le_deltav.setText("{:.2f}".format((deltaV)))
    ui.le_impulse.setText("{:.2f}".format((I)))
    ui.le_mr.setText("{:.2f}".format((MR)))
    ui.le_thrust.setText("{:.2f}".format((avg_thrust)))

def setupHandlers(ui):
    ui.pushButton.clicked.connect(lambda: calculate(ui))
    ui.le_apogee.setValidator(validator)
    ui.le_isp.setValidator(validator)
    ui.le_m0.setValidator(validator)
    ui.le_deltav.setValidator(validator)
    ui.le_impulse.setValidator(validator)
    ui.le_mr.setValidator(validator)
    ui.le_mr.setValidator(validator)
    ui.le_thrust.setValidator(validator)
    ui.le_thrust.setValidator(validator)

def initializeN3parameters(ui):
    ui.le_apogee.setText('2000.0')
    ui.le_isp.setText('110.0')
    ui.le_m0.setText('10.0')
    ui.le_burntime.setText('1.8')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    setupHandlers(ui)
    initializeN3parameters(ui)
    Form.show()
    sys.exit(app.exec_())
