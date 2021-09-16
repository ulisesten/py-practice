import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from datos import Rutas
from datos.ComputadorDAO import ComputadorDAO
from datos.RatonDAO import RatonDAO
from datos.Registro import Registro
from dominio.Computador import Computador
from gui.vtn_computador_ingresar import Ui_vtn_computador


class ServicioComputadorIngreso(QtWidgets.QMainWindow):
    def __init__(self):
        super(ServicioComputadorIngreso, self).__init__()
        self.ui = Ui_vtn_computador()
        self.ui.setupUi(self)
        self._raton = None
        self._pc =None
        self.cargar_ratones()
        self.ui.btn_guardar.clicked.connect(self.ingresar_computador)

    def cargar_ratones(self):
        #conexion a la BBDD para traer el listado de ratones
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


    def limpiar_formulario(self):
        self.ui.txt_descripcion.setText('')
        #self.ui.txt_marca.setText('')


    def ingresar_computador(self):
        if self.validar_datos():
            descripcion = self.ui.txt_descripcion.text().upper()
            nombre =  'nombre' #self.ui.txt_marca.text().upper()
            monitor = 'monitor'
            teclado = 'teclado' #self.ui.txt_cantidad_botones.text()
            ratonTableRow = self.ui.tb_ratones.currentRow()
            ratonTableIdColumn = self.ui.tb_ratones.item(ratonTableRow, 0)
            ratonId = 'raton_id' #ratonTableIdColumn.text()
            computador = Computador(nombre=descripcion, monitor=monitor, teclado=teclado, raton=ratonId)
            print(computador)
            if ComputadorDAO.insertar(computador)==1:
                self.ui.stb_estado.showMessage('Ingreso Exitoso',2000)
                self.limpiar_formulario()

            # if self.monstrar_mensaje('Raton', 'Ingreso Exitoso', QMessageBox.Information) == QMessageBox.Ok:
            #     self.limpiar_formulario()
        else:
            self.monstrar_mensaje('Computador', 'Debe completar todos los datos', QMessageBox.Warning)



    def validar_datos(self):
        if self.ui.txt_descripcion.text() == '':
            return False
        else:
            return True



    def monstrar_mensaje(self, titulo, mensaje, tipo):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(titulo)
        dlg.setText(mensaje)
        dlg.setIcon(tipo)
        return dlg.exec()




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = ServicioComputadorIngreso()
    application.show()
    sys.exit(app.exec_())