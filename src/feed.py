import os 
from PyQt5.QtGui import QPixmap
import PyQt5.QtCore as QtCore

def run(ui):
    pass

def initVariables(ui):
    pass

def loadImages(ui):
    path = os.path.dirname(os.path.abspath(__file__))
    ox_pid = QPixmap(os.path.join(path, './image/pid_ox.png'))
    ox_pid = ox_pid.scaled(ui.label_pid_ox.size(), QtCore.Qt.KeepAspectRatio)
    ui.label_pid_ox.setPixmap(ox_pid)
    fuel_pid = QPixmap(os.path.join(path, './image/pid_fuel.png'))
    fuel_pid = fuel_pid.scaled(ui.label_pid_fuel.size(), QtCore.Qt.KeepAspectRatio)
    ui.label_pid_fuel.setPixmap(fuel_pid)


def initialize(ui):
    initVariables(ui)
    loadImages(ui)