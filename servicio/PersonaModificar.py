import ast
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from datos import Rutas
from datos.PersonaDAO import PersonaDAO
from datos.Registro import Registro
from dominio.Persona import Persona
from gui.vtn_persona import Ui_vtn_Persona
from gui.vtn_persona_modificar import Ui_vtn_Persona_modificar


class PersonaModificar(QtWidgets.QMainWindow):
    def __init__(self):
        super(PersonaModificar, self).__init__()
        self.ui = Ui_vtn_Persona_modificar()
        self.ui.setupUi(self)
        self._persona = None
        self.ui.btn_buscar.clicked.connect(self.buscar)
        self.ui.btn_guardar.clicked.connect(self.guardar_datos)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_dato)


    def buscar(self):
        cedula = self.ui.txt_buscar_cedula.text()
        if cedula!= '':
            persona = Persona(cedula=cedula)
            self._persona = PersonaDAO.seleccionar_cedula(persona=persona)
            self.cargar_datos()
        else:
            QMessageBox.critical(self,'Error','Ingrese la cedula para buscar')

    #0123477777
    def cargar_datos(self):
        self.ui.txt_cedula.setText(self._persona.cedula)
        self.ui.txt_email.setText(self._persona.email)
        self.ui.txt_nombre.setText(self._persona.nombre)
        self.ui.txt_apellido.setText(self._persona.apellido)

    def borrar_formulario(self):
        self.ui.txt_cedula.clear()
        self.ui.txt_email.clear()
        self.ui.txt_nombre.clear()
        self.ui.txt_apellido.clear()
        self.ui.txt_buscar_cedula.clear()

    def guardar_datos(self):
        if self.validar_datos():
            nombre = self.ui.txt_nombre.text()
            cedula = self.ui.txt_cedula.text()
            email = self.ui.txt_email.text()
            telefono = self.ui.txt_telefono.text()
            self._persona.apellido = self.ui.txt_apellido.text()
            self._persona.cedula = cedula
            self._persona.email = email
            self._persona.nombre = nombre
            if PersonaDAO.actualizar(self._persona) == 1:
                self.ui.stb_estado.showMessage('Actualizacion exitosa',3000)
                self.borrar_formulario()
            else:
                QMessageBox.critical(self, 'Error', 'No se pudo actualizar la informacion de la persona.')
    def validar_datos(self):
        if self.ui.txt_nombre.text() != '' or self.ui.txt_cedula.text() != '' or self.ui.txt_email.text() != '' or self.ui.txt_apellido.text() != '':
             return True
        else:
            return False

    def eliminar_dato(self):
        self.buscar()

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirmar Eliminacion")
        dlg.setText("Esta seguro de eliminar los datos de la persona")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            if PersonaDAO.eliminar(self._persona) == 1:
                self.ui.stb_estado.showMessage('Eliminacion exitosa', 3000)
                self.borrar_formulario()
            else:
                QMessageBox.critical(self, 'Error', 'No se pudo eliminar la informacion de la persona.')
        else:
            pass









if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PersonaModificar()
    application.show()
    sys.exit(app.exec())