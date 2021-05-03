# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Examenfinal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Examenfinalv import Ui_MainWindow1
import Blanquita as bq

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-240, -290, 1061, 851))
        self.label.setStyleSheet("background-image: url(:/owo/probius_1920x1200.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 551, 311))
        self.plainTextEdit.setStyleSheet("background-image: url(:/owo/lost-odyssey-03b.jpg);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(570, 80, 113, 25))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(700, 80, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(630, 160, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(630, 240, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"URW Bookman L\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(710, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"URW Bookman L\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 130, 101, 21))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"URW Bookman L\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 200, 141, 21))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"URW Bookman L\";")
        self.label_5.setObjectName("label_5")
        self.PB_mostrart = QtWidgets.QPushButton(self.centralwidget)
        self.PB_mostrart.setGeometry(QtCore.QRect(450, 10, 101, 25))
        self.PB_mostrart.setObjectName("PB_mostrart")
        self.PB_mostrart.clicked.connect(self.openWindow)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 240, 26))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.PB_interpolar1 = QtWidgets.QPushButton(self.splitter)
        self.PB_interpolar1.setObjectName("PB_interpolar1")
        
        self.PB_interpolart = QtWidgets.QPushButton(self.splitter)
        self.PB_interpolart.setObjectName("PB_interpolart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###Botones aqui###
        self.PB_interpolar1.clicked.connect(self.mostrar)
        self.PB_interpolart.clicked.connect(self.i1)
        self.PB_interpolart.clicked.connect(self.i2)
        self.PB_interpolart.clicked.connect(self.i3)
        self.PB_interpolart.clicked.connect(self.i4)
        self.PB_interpolart.clicked.connect(self.i5)
        ###Funciones aqui###
    def i1(self):
        Linea = int(self.lineEdit_2.text())
        Tiempo = int(self.lineEdit_3.text())
        Porcentaje = str(self.lineEdit_4.text())
        owo = str(bq.zilean.int_todo1(Linea,Tiempo,Porcentaje))
        self.plainTextEdit.setStyleSheet("color:red")
        self.plainTextEdit.insertPlainText(owo+'\n')
        
    def i2(self):
        Linea = int(self.lineEdit_2.text())
        Tiempo = int(self.lineEdit_3.text())
        Porcentaje = str(self.lineEdit_4.text())
        owo = str(bq.zilean.int_todo2(Linea,Tiempo,Porcentaje))
        self.plainTextEdit.setStyleSheet("color:red")
        self.plainTextEdit.insertPlainText(owo+'\n')    
        
    def i3(self):
        Linea = int(self.lineEdit_2.text())
        Tiempo = int(self.lineEdit_3.text())
        Porcentaje = str(self.lineEdit_4.text())
        owo = str(bq.zilean.int_todo3(Linea,Tiempo,Porcentaje))
        self.plainTextEdit.setStyleSheet("color:red")
        self.plainTextEdit.insertPlainText(owo+'\n')    
        
    def i4(self):
        Linea = int(self.lineEdit_2.text())
        Tiempo = int(self.lineEdit_3.text())
        Porcentaje = str(self.lineEdit_4.text())
        owo = str(bq.zilean.int_todo4(Linea,Tiempo,Porcentaje))
        self.plainTextEdit.setStyleSheet("color:red")
        self.plainTextEdit.insertPlainText(owo+'\n')    
        
    def i5(self):
        Linea = int(self.lineEdit_2.text())
        Tiempo = int(self.lineEdit_3.text())
        Porcentaje = str(self.lineEdit_4.text())
        owo = str(bq.zilean.int_todo5(Linea,Tiempo,Porcentaje))
        self.plainTextEdit.setStyleSheet("color:red")
        self.plainTextEdit.insertPlainText(owo+'\n')
        
    def mostrar(self):
        Tabla = int(self.lineEdit_2.text())
        Linea = int(self.lineEdit_2.text())
        Tiempo = int(self.lineEdit_3.text())
        Porcentaje = str(self.lineEdit_4.text())
        owo = str(bq.zilean.int_tabla(Tabla,Linea,Tiempo,Porcentaje))
        self.plainTextEdit.setStyleSheet("color:red")
        self.plainTextEdit.insertPlainText(owo+'\n')
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "NA"))
        self.lineEdit_2.setText(_translate("MainWindow", "NA"))
        self.lineEdit_3.setText(_translate("MainWindow", "NA"))
        self.lineEdit_4.setText(_translate("MainWindow", "NA"))
        self.label_2.setText(_translate("MainWindow", "Tabla"))
        self.label_3.setText(_translate("MainWindow", "Linea"))
        self.label_4.setText(_translate("MainWindow", "Tiempo"))
        self.label_5.setText(_translate("MainWindow", "Porcentaje"))
        self.PB_mostrart.setText(_translate("MainWindow", "Mostrar tabla"))
        self.PB_interpolar1.setText(_translate("MainWindow", "Interpolar"))
        self.PB_interpolart.setText(_translate("MainWindow", "Interpolar todo"))

import qrcop

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

