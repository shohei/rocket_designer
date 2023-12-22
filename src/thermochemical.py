import numpy as np
from rocketcea.cea_obj import CEA_Obj

def convertMPaToPSI(mpa):
    return mpa * 145.037744

def convertRankineToKelvine(rankine):
    return rankine * 5/9

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
    IspArr = []
    mrArr = []
    gammaArr = []
    TcArr = []
    MWArr = []
    MR = 1.0
    while MR < 8.0:
        IspVac, Cstar, Tc, MW, gamma = ispObj.get_IvacCstrTc_ChmMwGam(Pc=Pc, MR=MR)
        cstarArr.append(Cstar)
        mrArr.append(MR)
        IspArr.append(IspVac)
        gammaArr.append(gamma)
        TcArr.append(convertRankineToKelvine(Tc))
        MWArr.append(MW)
        MR += 0.05

    maxIsp, optMR, optGamma, optTc, optMW = findMaxIsp(mrArr, IspArr, gammaArr, TcArr, MWArr)     
    mdot = float(ui.le_mdot.text())
    mdot_fuel = mdot/(1+optMR)
    mdot_ox =  optMR * mdot_fuel

    ui.le_max_isp.setText("{:.2f}".format(maxIsp))
    ui.le_opt_mr.setText("{:.2f}".format(optMR))
    ui.le_mdot_ox.setText("{:.2f}".format(mdot_ox))
    ui.le_mdot_fuel.setText("{:.2f}".format(mdot_fuel))
    ui.le_gamma.setText("{:.2f}".format(optGamma))
    ui.le_aft.setText("{:.2f}".format(optTc))
    ui.le_M.setText("{:.2f}".format(MW))

    ax.plot(mrArr, IspArr, label='Pc =%g psia'%Pc)
    ax.legend(loc='best')
    ax.grid(True)
    ax.set(xlabel='Mixture Ratio',
           ylabel='Isp vac.(sec)',
           title=ispObj.desc)

    canvas.draw()

def findMaxIsp(mrArr, IspArr, gammaArr, TcArr, MWArr):
    i = np.argmax(IspArr)
    maxIsp = IspArr[i]
    optMR = mrArr[i]
    optGamma = gammaArr[i] 
    optTc = TcArr[i]
    optMW = MWArr[i]    
    return (maxIsp, optMR, optGamma, optTc, optMW)

def initializeVariables(ui):
    ui.le_pc.setText('2.0')

def run(ui):
    computeCstar(ui)

def initialize(ui):
    initializeVariables(ui)
    computeCstar(ui)
