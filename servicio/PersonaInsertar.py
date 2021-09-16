import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtWidgets import QMessageBox

import dominio
from datos import Rutas
from datos.PersonaDAO import PersonaDAO
from datos.Registro import Registro
from gui.vtn_persona import Ui_vtn_Persona


class PersonaInsertar(QtWidgets.QMainWindow):
    def __init__(self):
        super(PersonaInsertar, self).__init__()
        self.ui = Ui_vtn_Persona()
        self.ui.setupUi(self)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.txt_telefono.setValidator(QtGui.QIntValidator())
        self.ui.btn_guardar.clicked.connect(self.guardar)


    def guardar(self):
        if self.validar_datos():
            nombre = self.ui.txt_nombre.text()
            cedula = self.ui.txt_cedula.text()
            email = self.ui.txt_email.text()
            telefono = self.ui.txt_telefono.text()
            apellido = self.ui.txt_apellido.text()

            persona = dominio.Persona.Persona(nombre=nombre, cedula=cedula, email=email, telefono=telefono, apellido=apellido)
            # if(Registro.guardar(persona, Rutas.PERSONAS)):
            insertar = PersonaDAO.insertar(persona)
            if(insertar == 1 ):
                self.ui.stb_estado.showMessage('Ingreso Exitoso',3000)
            elif(insertar == -2):
                self.monstrar_mensaje('Persona', 'Esta ingresando una persona repetida', QMessageBox.Warning)
            else:
                self.monstrar_mensaje('Persona', 'FAllo al ingresar la persona', QMessageBox.Warning)

    def validar_datos(self):
        if self.ui.txt_nombre.text() != '' or self.ui.txt_cedula.text() != '' or self.ui.txt_email.text() != '':
             return True
        else:
            return False

    def monstrar_mensaje(self, titulo, mensaje, tipo):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(titulo)
        dlg.setText(mensaje)
        dlg.setIcon(tipo)
        return dlg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PersonaInsertar()
    application.show()
    sys.exit(app.exec())