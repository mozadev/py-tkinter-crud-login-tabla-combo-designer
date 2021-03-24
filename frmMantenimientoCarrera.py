

'''
INTEGRANTES
MOZA REYES CESAR OSWALDO
TEJADA MORALES TERRY
TERRAZAS HUAMANI JORGE
QUISPE TICLLASUCA KEVIN
REYNA MIÑANO RONALDO
'''


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCarrera(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 356)
        self.etiquetaCodigo = QtWidgets.QLabel(Dialog)
        self.etiquetaCodigo.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.etiquetaCodigo.setObjectName("etiquetaCodigo")
        self.etiquetaNombre = QtWidgets.QLabel(Dialog)
        self.etiquetaNombre.setGeometry(QtCore.QRect(40, 80, 47, 13))
        self.etiquetaNombre.setObjectName("etiquetaNombre")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 241, 16))
        self.label_3.setObjectName("label_3")
        self.txtcodigoCarrera = QtWidgets.QLineEdit(Dialog)
        self.txtcodigoCarrera.setGeometry(QtCore.QRect(140, 40, 161, 20))
        self.txtcodigoCarrera.setObjectName("txtcodigoCarrera")
        self.txtnombreCarrera = QtWidgets.QLineEdit(Dialog)
        self.txtnombreCarrera.setGeometry(QtCore.QRect(140, 70, 161, 20))
        self.txtnombreCarrera.setObjectName("txtnombreCarrera")
        self.botonCarreraGrabar = QtWidgets.QPushButton(Dialog)
        self.botonCarreraGrabar.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.botonCarreraGrabar.setObjectName("botonCarreraGrabar")
        self.tablaCarrera = QtWidgets.QTableWidget(Dialog)
        self.tablaCarrera.setGeometry(QtCore.QRect(50, 150, 321, 192))
        self.tablaCarrera.setObjectName("tablaCarrera")
        self.tablaCarrera.setColumnCount(3)
        self.tablaCarrera.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCarrera.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCarrera.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaCarrera.setHorizontalHeaderItem(2, item)
        self.boton_modificar = QtWidgets.QPushButton(Dialog)
        self.boton_modificar.setGeometry(QtCore.QRect(180, 110, 75, 23))
        self.boton_modificar.setObjectName("boton_modificar")
        self.boton_eliminar = QtWidgets.QPushButton(Dialog)
        self.boton_eliminar.setGeometry(QtCore.QRect(290, 110, 75, 23))
        self.boton_eliminar.setObjectName("boton_eliminar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.etiquetaCodigo.setText(_translate("Dialog", "codigo: "))
        self.etiquetaNombre.setText(_translate("Dialog", "nombre : "))
        self.label_3.setText(_translate("Dialog", "Mantenimiento de la tabla carrera profesional"))
        self.botonCarreraGrabar.setText(_translate("Dialog", "grabar"))
        item = self.tablaCarrera.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "codigo "))
        item = self.tablaCarrera.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "nombre"))
        item = self.tablaCarrera.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "estado"))
        self.boton_modificar.setText(_translate("Dialog", "Modificar"))
        self.boton_eliminar.setText(_translate("Dialog", "Eliminar"))
