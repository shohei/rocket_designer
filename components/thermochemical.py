import numpy as np
from rocketcea.cea_obj import CEA_Obj

def convertMPaToPSI(mpa):
    return mpa * 145.037744

def computeCstar(ui):
    canvas = ui.plotWidget.canvas
    ax = canvas.ax
    ox = ui.cbox_ox.currentText()
    fuel = ui.cbox_fuel.currentText()
    ispObj = CEA_Obj(propName='', 
                     oxName=ox, 
                     fuelName=fuel) 
    Pc = convertMPaToPSI(float(ui.le_pc.text()))
    ax.clear()

    cstarArr = []
    MR = 1.0
    mrArr = []
    while MR < 8.0:
        cstarArr.append(ispObj.get_Cstar(Pc=Pc, MR=MR))
        mrArr.append(MR)
        MR += 0.05

    optMR = findMaxCstar(mrArr, cstarArr)     
    ui.le_opt_mr.setText("{:.2f}".format(optMR))

    ax.plot(mrArr, cstarArr, label='Pc =%g psia'%Pc)
    ax.legend(loc='best')
    ax.grid(True)
    ax.set(xlabel='Mixture Ratio',
           ylabel='C* (ft/sec)',
           title=ispObj.desc)

    canvas.draw()

def findMaxCstar(mrArr, cstarArr):
    i = np.argmax(cstarArr)
    optMR = mrArr[i]
    return optMR

def initializeVariables(ui):
    ui.le_pc.setText('2.0')

def run(ui):
    computeCstar(ui)

def setupHandlers(ui):
    ui.runThermalButton.clicked.connect(lambda: run(ui))

def initialize(ui):
    initializeVariables(ui)
    setupHandlers(ui)
    computeCstar(ui)
