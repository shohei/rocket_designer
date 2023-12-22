import math
from mpmath import sec
import pdb

def initVariables(ui):
    ui.le_pc_2.setText(ui.le_pc.text())
    ui.le_aft_2.setText(ui.le_aft.text())
    ui.le_gamma_2.setText(ui.le_gamma.text())
    ui.le_mdot_2.setText(ui.le_mdot.text())
    ui.le_M_2.setText(ui.le_M.text())
    ui.cbox_noztype.setCurrentIndex(0)
    ui.le_div_half_angle.setText('15')
    scaling_factor = 0.5 #0.5 to 1.5
    ui.le_scaling_nozzle.setText(str(scaling_factor))

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
    Dt = 2*math.sqrt(At/math.pi) #[m]
    De = 2*math.sqrt(Ae/math.pi) #[m]
    scaling_factor = float(ui.le_scaling_nozzle.text()) 
    Rt = Dt/2 #[m]
    Ru = scaling_factor * Rt #[m]
    divergence_half_angle = float(ui.le_div_half_angle.text()) #[deg]
    nozzle_efficiency = 0.5*(1+math.cos(divergence_half_angle/180*math.pi))
    Ln = float((Rt*(math.sqrt(e_opt)-1)+Ru*sec(divergence_half_angle/180*math.pi-1))/math.tan(divergence_half_angle/180*math.pi)) #[m]
    ui.le_at.setText("{:.2f}".format((At*1e6)))
    ui.le_dt.setText("{:.2f}".format((Dt*1e3)))
    ui.le_eopt.setText("{:.2f}".format((e_opt)))
    ui.le_ae.setText("{:.2f}".format((Ae*1e6)))
    ui.le_de.setText("{:.2f}".format((De*1e3)))
    ui.le_Ru.setText("{:.2f}".format((Ru*1e3)))
    ui.le_nozzle_efficiency.setText("{:.3f}".format(nozzle_efficiency))
    ui.le_Ln.setText("{:.2f}".format((Ln*1e3)))

def initialize(ui):
    initVariables(ui)
    run(ui)