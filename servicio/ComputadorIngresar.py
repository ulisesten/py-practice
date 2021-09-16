import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from datos.ComputadorDAO import ComputadorDAO
from datos.RatonDAO import RatonDAO
from dominio.Computador import Computador
from dominio.Raton import Raton
from gui.vtn_computador_ingresar import Ui_vtn_computador


class ComputadorIngresar(QtWidgets.QMainWindow):
    def __init__(self):
        super(ComputadorIngresar, self).__init__()
        self.ui = Ui_vtn_computador()
        self.ui.setupUi(self)
        self._raton = None
        self._pc =None
        self.cargar_ratones()
        self.ui.tb_ratones.itemClicked.connect(self.escoger_raton)
        self.ui.btn_guardar.clicked.connect(self.guardar)


    def escoger_raton(self):
        fila = self.ui.tb_ratones.currentRow()
        self.ui.tb_ratones.selectRow(fila)
        idraton = self.ui.tb_ratones.item(fila, 0).text()
        marca = self.ui.tb_ratones.item(fila, 1).text()
        entrada = self.ui.tb_ratones.item(fila, 2).text()
        cantidad = self.ui.tb_ratones.item(fila, 3).text()
        self._raton = Raton(idRaton=idraton, marca=marca, tipoEntrada=entrada,
                            cantidad_botones=cantidad)
        print(self._raton)


    def cargar_ratones(self):
        #conexion a la BBDD para traer el listado de personas
        ratones = RatonDAO.seleccionar()
        data = []
        for raton in ratones:
            data.append((str(raton.idRaton),raton.marca, raton.tipoEntrada,
                         str(raton.cant_botones)))
        fila = 0
        for registro in data:
            columna = 0
            self.ui.tb_ratones.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.ui.tb_ratones.setItem(fila, columna, celda)
                columna += 1
            fila += 1

    def guardar(self):
        desc = self.ui.txt_descripcion.text()
        self._pc = Computador(nombre=desc, raton=self._raton)
        print(self._pc)
        ComputadorDAO.insertar(self._pc)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = ComputadorIngresar()
    application.show()
    sys.exit(app.exec())