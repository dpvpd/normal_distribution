# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import sys
import math
import matplotlib.pyplot as plt

dir = os.getcwd() + '\\'
_translate = QtCore.QCoreApplication.translate
ui = uic.loadUiType(dir+'main.ui')[0]

def f(x,m,v):
    a = ((2*math.pi*v)**(1/2))
    b = (-1) * (((x-m)**2) / (2*v))
    c = math.exp(1) ** b
    return a * c


class Form(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setFixedSize(201,109)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pmfunc)
        self.pushButton_2.clicked.connect(self.close)

        self.show()

    def pmfunc(self):
        m = self.spinBox.value()
        v = self.spinBox_2.value()

        s = round(m-(v/2))
        e = round(m+(v/2))
        
        x = []
        y = []
        for i in range(s, e+1):
            x.append(i)
            y.append(f(i,m,v))
        plt.bar(x,y,width=0.7)
        plt.show()
        return

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())