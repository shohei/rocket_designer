# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cheatsheet.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cs_form(object):
    def setupUi(self, cs_form):
        cs_form.setObjectName("cs_form")
        cs_form.resize(501, 652)
        self.webViewWidget = WebViewWidget(cs_form)
        self.webViewWidget.setGeometry(QtCore.QRect(30, 30, 441, 571))
        self.webViewWidget.setObjectName("webViewWidget")

        self.retranslateUi(cs_form)
        QtCore.QMetaObject.connectSlotsByName(cs_form)

    def retranslateUi(self, cs_form):
        _translate = QtCore.QCoreApplication.translate
        cs_form.setWindowTitle(_translate("cs_form", "Cheatsheet"))
from webviewwidget import WebViewWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cs_form = QtWidgets.QWidget()
    ui = Ui_cs_form()
    ui.setupUi(cs_form)
    cs_form.show()
    sys.exit(app.exec_())
