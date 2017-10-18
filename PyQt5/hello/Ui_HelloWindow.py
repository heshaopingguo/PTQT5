# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\work\software\PyQt5\hello\HelloWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.Button_ok = QtWidgets.QPushButton(Dialog)
        self.Button_ok.setGeometry(QtCore.QRect(70, 160, 82, 25))
        self.Button_ok.setObjectName("Button_ok")
        self.Button_close = QtWidgets.QPushButton(Dialog)
        self.Button_close.setGeometry(QtCore.QRect(220, 160, 82, 25))
        self.Button_close.setObjectName("Button_close")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 90, 63, 13))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.Button_close.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_ok.setText(_translate("Dialog", "确定"))
        self.Button_close.setText(_translate("Dialog", "关闭"))
        self.label.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

