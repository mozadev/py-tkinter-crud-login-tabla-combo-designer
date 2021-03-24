'''
INTEGRANTES
MOZA REYES CESAR OSWALDO
TEJADA MORALES TERRY
TERRAZAS HUAMANI JORGE
QUISPE TICLLASUCA KEVIN
REYNA MIÑANO RONALDO
'''



import  sys
import random
from frmMenuPrincipal import *
from frmMantenimientoCarrera import *
from frmManteMateria import *
from tkinter import messagebox, ttk
from PyQt5.QtWidgets import QMessageBox


listanombresCarreras=[]
listaCarreras=[]
listaMaterias=[]
registros=0

listaCarrerasProfesional=[]

class Miformulario(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.conectarFrmCarrera)
        self.ui.pushButton_2.clicked.connect(self.conectarFrmMateria)
        self.ventaCarrera=frmMantenimientoCarrera()
        self.ventanaMateria=frmMantenimientoMateria()


    def conectarFrmCarrera(self):
        self.ventaCarrera.exec_()

    def conectarFrmMateria(self):
        self.ventanaMateria.exec_()

class frmMantenimientoCarrera(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui=Ui_DialogCarrera()
        self.ui.setupUi(self)

        self.ui.botonCarreraGrabar.clicked.connect(self.cargarDatosTabla)
        self.ui.boton_eliminar.clicked.connect( lambda: self.ui.tablaCarrera.removeRow(self.ui.tablaCarrera.currentRow()))

        self.ui.boton_eliminar.clicked.connect(self.eliminar_fila_carrera)
        self.ui.boton_modificar.clicked.connect(self.modificar_fila_carrera)

    def modificar_fila_carrera(self):
        if len(self.ui.txtcodigoCarrera.text()) != 0 and len(self.ui.txtnombreCarrera.text()) != 0:
            carreras = {}
            carreras["codigo"] = self.ui.txtcodigoCarrera.text()
            carreras["nombre"] = self.ui.txtnombreCarrera.text()
            carreras["estado"] = "activado"
            listaCarreras.insert(self.ui.tablaCarrera.currentRow(),carreras)
            listaCarreras.pop(self.ui.tablaCarrera.currentRow()+1)

            row = 0
            self.ui.tablaCarrera.setRowCount(len(listaCarreras))

            for carrera in listaCarreras:
                self.ui.tablaCarrera.setItem(row, 0, QtWidgets.QTableWidgetItem(str(carrera["codigo"])))
                self.ui.tablaCarrera.setItem(row, 1, QtWidgets.QTableWidgetItem(str(carrera["nombre"])))
                self.ui.tablaCarrera.setItem(row, 2, QtWidgets.QTableWidgetItem(str(carrera["estado"])))
                row = row + 1

                self.ui.txtcodigoCarrera.clear()
                self.ui.txtnombreCarrera.clear()
                self.ui.txtcodigoCarrera.setFocus()
        else:
         QMessageBox.warning(self,"formulario incorrecto","validacion incorrecto",QMessageBox.Discard)

    def eliminar_fila_carrera(self):

        if len(listaCarreras) > 0:
            listaCarreras.pop(self.ui.tablaCarrera.currentRow())
        else:
            QMessageBox.warning(self, "error de validacion", "no se selecciono ningun valor", QMessageBox.Discard)

    def cargarDatosTabla(self):
        if len(self.ui.txtcodigoCarrera.text()) != 0 and len(self.ui.txtnombreCarrera.text()) != 0:
            carreras = {}
            carreras["codigo"] =self.ui.txtcodigoCarrera.text()
            carreras["nombre"]=self.ui.txtnombreCarrera.text()
            carreras["estado"]="activado"
            listaCarreras.append(carreras)
            listanombresCarreras.append(carreras["nombre"])


            row=0
            self.ui.tablaCarrera.setRowCount(len(listaCarreras))

            for carrera in listaCarreras:
                self.ui.tablaCarrera.setItem(row, 0, QtWidgets.QTableWidgetItem(str(carrera["codigo"])))
                self.ui.tablaCarrera.setItem(row, 1, QtWidgets.QTableWidgetItem(str(carrera["nombre"])))
                self.ui.tablaCarrera.setItem(row, 2, QtWidgets.QTableWidgetItem(str(carrera["estado"])))
                row = row + 1


                self.ui.txtcodigoCarrera.clear()
                self.ui.txtnombreCarrera.clear()
                self.ui.txtcodigoCarrera.setFocus()

        else:
         QMessageBox.warning(self,"formulario incorrecto","validacion incorrecto",QMessageBox.Discard)


class frmMantenimientoMateria(QtWidgets.QDialog):

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_DialogMateria()
        self.ui.setupUi(self)
        self.ui.botongrabarMateria.clicked.connect(self.cargar_datos_materia)
        #self.ui.comboBoxCarrera.currentIndexChanged.connect(self.selecciona_carrera)
        self.ui.botonEliminarMateria.clicked.connect(lambda: self.ui.tablaMateria.removeRow(self.ui.tablaMateria.currentRow()))
        self.ui.botonEliminarMateria.clicked.connect(self.eliminar_fila)

        self.ui.botonModificarMateria.clicked.connect(self.modificar_fila_materia)


        listaCarrerasProfesional = ["administracion", "sistemas", "ingenieria industrial", "contabilidad"]

        for i in listaCarrerasProfesional:
            self.ui.comboBoxCarrera.addItem(str(i))
    #def elimiar_fila_tabla(self):
        #lambda: self.ui.tablaMateria.removeRow(self.ui.tablaMateria.currentRow())
    #def validation(self):
        # selected_item = self.ui.tablaMateria.selectionMode()
        # values = tuple(self.ui.tablaMateria.item(self,1,1)
        # return len(values) != 0
        # return len(selected_item) != 0


    def eliminar_fila(self):


        if len(listaMaterias)>0:
            listaMaterias.pop(self.ui.tablaMateria.currentRow())
        else:
            QMessageBox.warning(self, "error de validacion", "no se selecciono ningun valor", QMessageBox.Discard)


        # if self.ui.tablaMateria.currentRow() == 0 or self.ui.tablaMateria.currentRow() >= 0:
        #     listaMaterias.pop(self.ui.tablaMateria.currentRow())
        # if len(tuple(self.ui.tablaMateria.currentItem(self.ui.tablaMateria.items()['values'])))==0:
        #     QMessageBox.warning(self,"error de validacion","no se selecciono ningun valor",QMessageBox.Discard)

    def modificar_fila_materia(self):
        if len(self.ui.txtCodigoMateria.text()) != 0 and len(self.ui.txtmateria.text()) != 0:
            materias = {}

            materias["codigo"] = self.ui.txtCodigoMateria.text()
            materias["carrera"] = self.ui.comboBoxCarrera.itemText(self.ui.comboBoxCarrera.currentIndex())
            materias["nombre"] = self.ui.txtmateria.text()
            materias["estado"] = "activado"
            listaMaterias.insert(self.ui.tablaMateria.currentRow(),materias)
            listaMaterias.pop(self.ui.tablaMateria.currentRow()+1)

            row = 0
            self.ui.tablaMateria.setRowCount(len(listaMaterias))

            for mate in listaMaterias:
                self.ui.tablaMateria.setItem(row, 0, QtWidgets.QTableWidgetItem(str(mate["codigo"])))
                self.ui.tablaMateria.setItem(row, 1, QtWidgets.QTableWidgetItem(str(mate["carrera"])))
                self.ui.tablaMateria.setItem(row, 2, QtWidgets.QTableWidgetItem(str(mate["nombre"])))
                self.ui.tablaMateria.setItem(row, 3, QtWidgets.QTableWidgetItem(str(mate["estado"])))
                row = row + 1
                self.ui.txtmateria.clear()
                self.ui.txtCodigoMateria.clear()
                self.ui.comboBoxCarrera.clear()
                self.ui.txtCodigoMateria.setFocus()

            listaCarrerasProfesional = ["administracion", "sistemas", "ingenieria industrial", "contabilidad"]

            for i in listaCarrerasProfesional:
                self.ui.comboBoxCarrera.addItem(str(i))

        else:
         QMessageBox.warning(self,"formulario incorrecto","validacion incorrecto",QMessageBox.Discard)


    def cargar_datos_materia(self):

        if len(self.ui.txtCodigoMateria.text()) != 0 and len(self.ui.txtmateria.text()) != 0:
            materias = {}

            materias["codigo"] = self.ui.txtCodigoMateria.text()
            materias["carrera"] = self.ui.comboBoxCarrera.itemText(self.ui.comboBoxCarrera.currentIndex())
            materias["nombre"] = self.ui.txtmateria.text()
            materias["estado"] = "activado"
            listaMaterias.append(materias)


            row = 0
            self.ui.tablaMateria.setRowCount(len(listaMaterias))

            for mate in listaMaterias:
                self.ui.tablaMateria.setItem(row, 0, QtWidgets.QTableWidgetItem(str(mate["codigo"])))
                self.ui.tablaMateria.setItem(row, 1, QtWidgets.QTableWidgetItem(str(mate["carrera"])))
                self.ui.tablaMateria.setItem(row, 2, QtWidgets.QTableWidgetItem(str(mate["nombre"])))
                self.ui.tablaMateria.setItem(row, 3, QtWidgets.QTableWidgetItem(str(mate["estado"])))
                row = row + 1
                self.ui.txtmateria.clear()
                self.ui.txtCodigoMateria.clear()
                self.ui.comboBoxCarrera.clear()
                self.ui.txtCodigoMateria.setFocus()

            listaCarrerasProfesional = ["administracion", "sistemas", "ingenieria industrial", "contabilidad"]

            for i in listaCarrerasProfesional:
                self.ui.comboBoxCarrera.addItem(str(i))

        else:
         QMessageBox.warning(self,"formulario incorrecto","validacion incorrecto",QMessageBox.Discard)

if __name__== "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mi_app=Miformulario()
    mi_app.show()
    sys.exit(app.exec_())

    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())
