# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_123 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
#        self.lineEdit.setText('')
#        print (sdfghjk)
#        print ('gggggg')
        self.lineEdit.setText('')
#        self.textBrowser.setText('')
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
#        print (self.lineEdit.text())
        my_str=self.lineEdit.text()
#        self.textBrowser.setText(my_str)
        self.textBrowser.append(my_str)

    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print (self.textBrowser.toPlainText())

    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r1')
        if self.radioButton_4.isChecked():
            print ('r4 is checked')
        elif self.radioButton_5.isChecked():
            print ('r5 is checked')
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r2')
        self.radioButton_4.setChecked(True)

    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r3')
        self.radioButton_5.setChecked(True)
    @pyqtSlot()
    def on_radioButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r5')
    @pyqtSlot()
    def on_radioButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r4')
    
    @pyqtSlot()
    def on_radioButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r6')
        self.textBrowser.setReadOnly(True)
        self.setWindowTitle('复选框')
    @pyqtSlot()
    def on_radioButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print ('you select r7')
        self.textBrowser.setReadOnly(False)

    
    @pyqtSlot(int)
    def on_dial_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        print (value)
        self.lcdNumber.display(value)
#        self.progressBar.display(value)

    
    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
#        raise NotImplementedError
        print (value)
        self.lcdNumber.display(value)
    @pyqtSlot(int)
    def on_verticalSlider_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
#        raise NotImplementedError

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
#        raise NotImplementedError
        my_button=QMessageBox.information(self,'提示', u"提示信息")
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError        
        my_button=QMessageBox.question(self, '询问','是否保存?')
        print (my_button)
        
    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
#        raise NotImplementedError
        my_button=QMessageBox.warning(self, 'warning','文字编码不同')
        print (my_button)
        
    @pyqtSlot()
    def on_pushButton_12_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
#        raise NotImplementedError
        my_button=QMessageBox.critical(self, '问题严重', '要出事了')
        print (my_button)
        
    @pyqtSlot()
    def on_pushButton_13_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError 
        my_button=QMessageBox.about(self, '关于', '这是我的程序软件，在学习这么长时间后觉得很有收获，这是对话框的使用。')
    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
#        raise NotImplementedError
        my_button=QMessageBox.aboutQt(self, '介绍QT')
    @pyqtSlot()
    def on_pushButton_15_clicked(self):
        """
        Slot documentation goes here.
        """
#        # TODO: not implemented yet
#        raise NotImplementedError
        #InputDialog.getText(self,'字符串',QLineEdit)
#        QInputDialog.getText(self, '字符串', 'please input information',  QLineEdit.Normal, '在此输入信息')
#        QInputDialog.getInt(self, '输入整数', '请输入一个整数，别的不要',  30, 0, 100)
        my_list=QStringList()
        my_list.append('香蕉')
        my_list.append('苹果')
        my_list.append('梨')
        my_list.append('橘子')
        my_str, ok=QInputDialog.getItemId(self, '下拉框','请选择', my_list)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
