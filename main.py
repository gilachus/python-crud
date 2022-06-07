from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys 
import conexion

def agregar():
    nombre = ventana.txtNombre.text()
    correo = ventana.txtCorreo.text()
    objContactos = conexion.contactos()
    result = objContactos.crearContacto((nombre,correo))
    consultar()

def editar():
    id = ventana.txtID.text()
    if(id):
        nombre = ventana.txtNombre.text()
        correo = ventana.txtCorreo.text()
        objContactos = conexion.contactos()
        result = objContactos.editarContacto((nombre,correo,id))
        consultar()

def eliminar(): 
    id = ventana.txtID.text()
    if id:
        objContactos = conexion.contactos()
        result = objContactos.eliminarContacto(id)
        consultar()

def cancelar():
    consultar()

def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl = 0
    objContactos = conexion.contactos()
    result = objContactos.leerContactos()
    for contacto in result:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl, 0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl, 1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl, 2, QTableWidgetItem(str(contacto[2])))
        indiceControl += 1
    ventana.TxtID.setText("")
    ventana.TxtNombre.setText("")
    ventana.TxtCorreo.setText("")
    ventana.btnAgregar.setEnable(True)
    ventana.btnEliminar.setEnable(False)
    ventana.btnModificar.setEnable(False)
    ventana.btnCancelar.setEnable(False)

def seleccionar():
    id     = ventana.tblContactos.selectedIndexes()[0].data()
    nombre = ventana.tblContactos.selectedIndexes()[1].data()
    correo = ventana.tblContactos.selectedIndexes()[2].data()
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)
    ventana.btnAgregar.setEnable(False)
    ventana.btnEliminar.setEnable(True)
    ventana.btnModificar.setEnable(True)
    ventana.btnCancelar.setEnable(True)

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi('ventana.ui')
ventana.show()
consultar()

ventana.tblContactos.setHorizontalHeaderLabels(['ID','Nombre','Correo'])
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContactos.cellClicked.connect(seleccionar)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEditar.clicked.connect(editar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())