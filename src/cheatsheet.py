from webviewwidget import WebViewWidget

def show(ui, ui_cs, cs_form):
    currentTabIndex = ui.tabWidget.currentIndex()
    docs = ['mission',
            'thermochemical',
            'nozzle',
            'chamber',
            'feed',
            'ignitor',
            'injector',
            'grain']
    doc = docs[currentTabIndex]
    file_location  = './doc/'+doc+'.html'
    ui_cs.webViewWidget.load(file_location)
    cs_form.show()

def initialize(ui, ui_cs, cs_form):
    pass
