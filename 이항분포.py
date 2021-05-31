# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import sys
import matplotlib.pyplot as plt

dir = os.getcwd() + '\\'
_translate = QtCore.QCoreApplication.translate
ui = uic.loadUiType(dir+'main.ui')[0]

def fac(n):
    a = 1
    for i in range(1,n+1):
        a*=i
    return a

def C(n,r):
    a = fac(n)
    b = fac(n-r)
    c = fac(r)
    return a / (b*c)


class Form(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setFixedSize(201,109)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pmfunc)
        self.pushButton_2.clicked.connect(self.close)

        self.show()

    def pmfunc(self):
        n = self.spinBox.value()
        p = self.doubleSpinBox.value()
        q = 1-p

        x = list(range(n+1))
        print(x)
        y = []
        for i in x:
            a = p**i
            b = q**(n-i)
            c = C(n,i)
            y.append(a*b*c)
        plt.bar(x,y,width=0.7)
        plt.show()
        s = 'E(x) = ' + str(n*p) + '\nV(x) = '+str(n*p*q)+'\nσ(x) = '+str((n*p*q)**(1/2))
        QtWidgets.QMessageBox.information(None,'계산 결과',s,QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.Yes)
        return

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())