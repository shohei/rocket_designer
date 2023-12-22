def setupHandlers(ui, ui_exp):
    ui_exp.nakuja_n3_button.clicked.connect(lambda: updateNakujaN3parameters(ui))
    ui_exp.usc_traveler4_button.clicked.connect(lambda: updateUSCTraveler4parameters(ui))
    ui_exp.jaxa_ss520_button.clicked.connect(lambda: updateJAXASS520parameters(ui))
    ui_exp.nakuja_liquid1_button.clicked.connect(lambda: updateNakujaLiquid1parameters(ui))
    ui_exp.jaxa_h3_button.clicked.connect(lambda: updateJAXAH3parameters(ui))
    ui_exp.spacex_falcon9_button.clicked.connect(lambda: updateSpaceXFalcon9parameters(ui))

def updateNakujaN3parameters(ui):
    ui.le_apogee.setText('2.0')
    ui.le_isp.setText('110.0')
    ui.le_m0.setText('10.0')
    ui.le_burntime.setText('1.8')

def updateUSCTraveler4parameters(ui):
    ui.le_apogee.setText('103.5714')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def updateJAXASS520parameters(ui):
    ui.le_apogee.setText('800.0')
    ui.le_isp.setText('282.6')
    ui.le_m0.setText('2740.0')
    ui.le_burntime.setText('25.6')

def updateNakujaLiquid1parameters(ui):
    ui.le_apogee.setText('N/A')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def updateJAXAH3parameters(ui):
    ui.le_apogee.setText('N/A')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def updateSpaceXFalcon9parameters(ui):
    ui.le_apogee.setText('N/A')
    ui.le_isp.setText('N/A')
    ui.le_m0.setText('N/A')
    ui.le_burntime.setText('N/A')

def initialize(ui, ui_exp):
    setupHandlers(ui, ui_exp)