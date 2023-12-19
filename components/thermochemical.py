import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        t = np.arange(0.0, 3.0, 0.01)
        s = 1 + np.sin(2*np.pi*t)
        fig, ax = plt.subplots()
        ax.plot(t,s)
        ax.set(xlabel='time',ylabel='voltage',title='About as simple as it gets, folks')
        ax.grid()

def initialize(ui):
    MplCanvas(ui)


