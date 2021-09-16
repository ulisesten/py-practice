import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from datos.PersonaDAO import PersonaDAO
from gui.vtn_persona_cargar import Ui_vtn_cargar_personas


class PersonaCargar(QtWidgets.QMainWindow):
    def __init__(self):
        super(PersonaCargar, self).__init__()
        self.ui = Ui_vtn_cargar_personas()
        self.ui.setupUi(self)
        self.cargar()
        self.ui.tb_personas.itemClicked.connect(self.mostrar)
        # item = self.ui.tb_personas.selectedItems()
        # self.ui.txt_idPersona = item[0].text()

    def mostrar(self):

        fila = self.ui.tb_personas.currentRow()
        self.ui.tb_personas.selectRow(fila)
        print(fila)
        # self.tbl_anggota.item(r, 0).text()
        self.ui.txt_idPersona.setText(self.ui.tb_personas.item(fila, 0).text())




    def cargar(self):
        #conexion a la BBDD para traer el listado de personas
        personas = PersonaDAO.seleccionar()
        data = []
        for persona in personas:
            data.append((str(persona.id_persona),persona.cedula, persona.nombre,
                         persona.apellido, persona.email))
        fila = 0
        for registro in data:
            columna = 0
            self.ui.tb_personas.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.ui.tb_personas.setItem(fila, columna, celda)
                columna += 1
            fila += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PersonaCargar()
    application.show()
    sys.exit(app.exec())