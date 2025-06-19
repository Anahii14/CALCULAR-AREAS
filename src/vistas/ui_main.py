from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction

class Ui_AreaCalculator(object):
    def setupUi(self, AreaCalculator1):
        AreaCalculator1.setObjectName("AreaCalculator")
        AreaCalculator1.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(AreaCalculator1)
        self.centralwidget.setObjectName("centralwidget")
        AreaCalculator1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AreaCalculator1)
        self.menubar.setObjectName("menubar")
        self.menuFiguras = QtWidgets.QMenu(self.menubar)
        self.menuFiguras.setObjectName("menuFiguras")
        AreaCalculator1.setMenuBar(self.menubar)
        self.actionCirculo = QAction(AreaCalculator1)
        self.actionCirculo.setObjectName("actionCirculo")
        self.actionTriangulo = QAction(AreaCalculator1)
        self.actionTriangulo.setObjectName("actionTriangulo")
        self.actionRectangulo = QAction(AreaCalculator1)
        self.actionRectangulo.setObjectName("actionRectangulo")
        self.actionCuadrado = QAction(AreaCalculator1)
        self.actionCuadrado.setObjectName("actionCuadrado")
        self.menubar.addAction(self.menuFiguras.menuAction())
        self.menuFiguras.addAction(self.actionCirculo)
        self.menuFiguras.addAction(self.actionTriangulo)
        self.menuFiguras.addAction(self.actionRectangulo)
        self.menuFiguras.addAction(self.actionCuadrado)

        self.retranslateUi(AreaCalculator1)
        QtCore.QMetaObject.connectSlotsByName(AreaCalculator1)

    def retranslateUi(self, AreaCalculator):
        _translate = QtCore.QCoreApplication.translate
        AreaCalculator.setWindowTitle(_translate("AreaCalculator", "Calculadora de Áreas"))
        self.menuFiguras.setTitle(_translate("AreaCalculator", "Figuras"))
        self.actionCirculo.setText(_translate("AreaCalculator", "Círculo"))
        self.actionTriangulo.setText(_translate("AreaCalculator", "Triángulo"))
        self.actionRectangulo.setText(_translate("AreaCalculator", "Rectángulo"))
        self.actionCuadrado.setText(_translate("AreaCalculator", "Cuadrado"))