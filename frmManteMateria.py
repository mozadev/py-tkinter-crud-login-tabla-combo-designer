'''
INTEGRANTES
MOZA REYES CESAR OSWALDO
TEJADA MORALES TERRY
TERRAZAS HUAMANI JORGE
QUISPE TICLLASUCA KEVIN
REYNA MIÑANO RONALDO
'''



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogMateria(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.botongrabarMateria = QtWidgets.QPushButton(Dialog)
        self.botongrabarMateria.setGeometry(QtCore.QRect(40, 110, 101, 23))
        self.botongrabarMateria.setObjectName("botongrabarMateria")
        self.txtmateria = QtWidgets.QLineEdit(Dialog)
        self.txtmateria.setGeometry(QtCore.QRect(160, 70, 161, 20))
        self.txtmateria.setObjectName("txtmateria")
        self.comboBoxCarrera = QtWidgets.QComboBox(Dialog)
        self.comboBoxCarrera.setGeometry(QtCore.QRect(160, 40, 161, 22))
        self.comboBoxCarrera.setObjectName("comboBoxCarrera")
        self.tablaMateria = QtWidgets.QTableWidget(Dialog)
        self.tablaMateria.setGeometry(QtCore.QRect(30, 150, 351, 121))
        self.tablaMateria.setObjectName("tablaMateria")
        self.tablaMateria.setColumnCount(4)
        self.tablaMateria.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMateria.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMateria.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMateria.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaMateria.setHorizontalHeaderItem(3, item)
        self.botonModificarMateria = QtWidgets.QPushButton(Dialog)
        self.botonModificarMateria.setGeometry(QtCore.QRect(210, 110, 75, 23))
        self.botonModificarMateria.setObjectName("botonModificarMateria")
        self.botonEliminarMateria = QtWidgets.QPushButton(Dialog)
        self.botonEliminarMateria.setGeometry(QtCore.QRect(300, 110, 75, 23))
        self.botonEliminarMateria.setObjectName("botonEliminarMateria")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 47, 13))
        self.label_3.setObjectName("label_3")
        self.txtCodigoMateria = QtWidgets.QLineEdit(Dialog)
        self.txtCodigoMateria.setGeometry(QtCore.QRect(160, 10, 161, 20))
        self.txtCodigoMateria.setObjectName("txtCodigoMateria")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "carrera: "))
        self.label_2.setText(_translate("Dialog", "nombre materia: "))
        self.botongrabarMateria.setText(_translate("Dialog", "grabar Materia"))
        item = self.tablaMateria.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "codigo"))
        item = self.tablaMateria.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "carrera"))
        item = self.tablaMateria.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Materia"))
        item = self.tablaMateria.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Estado"))
        self.botonModificarMateria.setText(_translate("Dialog", "Modificar"))
        self.botonEliminarMateria.setText(_translate("Dialog", "Eliminar"))
        self.label_3.setText(_translate("Dialog", "codigo"))
