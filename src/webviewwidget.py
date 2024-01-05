import os
from PyQt5.QtWidgets  import QWidget 
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWidgets import QVBoxLayout

class WebViewWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay = QVBoxLayout(self)
    
    def load(self, file_location):
        if hasattr(self, 'view'):
            self.lay.removeWidget(self.view)
        self.view = QtWebEngineWidgets.QWebEngineView()
        path = os.path.dirname(os.path.abspath(__file__))
        url = QUrl.fromLocalFile(os.path.join(path, file_location))
        self.view.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.view.load(url)
        self.lay.addWidget(self.view)