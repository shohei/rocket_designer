import math

def initVariables(ui):
    ui.le_pc_2.setText(ui.le_pc.text())
    ui.le_aft_2.setText(ui.le_aft.text())
    ui.le_gamma_2.setText(ui.le_gamma.text())
    ui.le_mdot_2.setText(ui.le_mdot.text())
    ui.le_M_2.setText(ui.le_M.text())

def run(ui):
    k = float(ui.le_gamma_2.text())
    Pc = float(ui.le_pc_2.text())*1e6 # [Pa] chamber pressure
    mdot = float(ui.le_mdot_2.text())   
    Tc = float(ui.le_aft_2.text())
    Rbar = 7391.0 # [J/kgK] universal gas constant
    R = Rbar/float(ui.le_M_2.text())
    At = mdot/Pc*math.sqrt(R*Tc/k)*(1+(k-1)/2)**((k+1)/(2*(k-1))) # [m^2] throat area
    Pe = 0.1013*1e6 #[Pa] atmospheric pressure
    At_Ae = ((k+1)/2)**(1/(k-1))*(Pe/Pc)**(1/k)*math.sqrt((k+1)/(k-1)*(1-(Pe/Pc)**((k-1)/k)))
    e_opt = 1/At_Ae
    Ae = At*e_opt
    Dt = 2*math.sqrt(At/math.pi)
    De = 2*math.sqrt(Ae/math.pi)
    ui.le_at.setText("{:.2f}".format((At*1e6)))
    ui.le_dt.setText("{:.2f}".format((Dt*1e3)))
    ui.le_eopt.setText("{:.2f}".format((e_opt)))
    ui.le_ae.setText("{:.2f}".format((Ae*1e6)))
    ui.le_de.setText("{:.2f}".format((De*1e3)))

def initialize(ui):
    initVariables(ui)
    run(ui)