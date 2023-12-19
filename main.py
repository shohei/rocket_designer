import sys
from ui import Ui_Form
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout)
from PyQt5.QtCore import Qt


def calculate(ui):
    print("calculate")
    # str = ui.le_apogee.copy()
    # ui.le_apogee.
    # print(str)
    ui.le_deltav.setText("Hello World")
    ui.le_impulse.setText("Hello World")
    ui.le_mr.setText("Hello World")

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

