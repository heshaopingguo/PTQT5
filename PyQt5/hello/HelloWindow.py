# -*- coding: utf-8 -*-

"""
Module implementing HelloWindow.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication

from Ui_HelloWindow import Ui_Dialog


class HelloWindow(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(HelloWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_Button_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label.setText('这是我的第一个 PyQt5 程序')
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dlg = HelloWindow()
    dlg.show()
    sys.exit(app.exec_())
