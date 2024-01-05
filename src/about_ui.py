# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(400, 300)
        AboutForm.setAcceptDrops(False)
        self.label = QtWidgets.QLabel(AboutForm)
        self.label.setGeometry(QtCore.QRect(170, 10, 181, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutForm)
        self.label_2.setGeometry(QtCore.QRect(176, 80, 191, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(AboutForm)
        self.textBrowser.setGeometry(QtCore.QRect(90, 140, 241, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.logo_label = QtWidgets.QLabel(AboutForm)
        self.logo_label.setGeometry(QtCore.QRect(60, 20, 100, 100))
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setObjectName("logo_label")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "About"))
        self.label.setText(_translate("AboutForm", "<html><head/><body><p><span style=\" font-size:24pt;\">Rocket Designer</span></p></body></html>"))
        self.label_2.setText(_translate("AboutForm", "Copyright ©2023 Shohei Aoki"))
        self.textBrowser.setHtml(_translate("AboutForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rocket designer is using the following open source software</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- RocketCEA</p></body></html>"))
        self.logo_label.setText(_translate("AboutForm", "Logo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutForm = QtWidgets.QWidget()
    ui = Ui_AboutForm()
    ui.setupUi(AboutForm)
    AboutForm.show()
    sys.exit(app.exec_())
