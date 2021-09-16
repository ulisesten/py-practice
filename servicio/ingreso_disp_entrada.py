import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from datos import Rutas
from datos.Registro import Registro
from dominio.Raton import Raton
from dominio.Teclado import Teclado
from gui.vtn_disp_entrada_ingresar import Ui_vtn_disp_entrada_ingresar


class ServicioDispEntradaIngreso(QtWidgets.QMainWindow):
    # entradas = ['USB', 'PS/2', 'Bluetooth', 'Wirelees', 'MicroUSB']
    def __init__(self):
        super(ServicioDispEntradaIngreso, self).__init__()
        self.ui_de = Ui_vtn_disp_entrada_ingresar()
        self.ui_de.setupUi(self)
        self.ui_de.btn_guardar.clicked.connect(self.ingresar)
        entradas = Registro.leer(Rutas.ENTRADAS)
        for entrada in entradas:
            self.ui_de.cb_tipo_entrada.addItem(entrada)

    def ingresar(self):
        marca = self.ui_de.txt_marca.text()
        if marca != '':
            tipo =  self.ui_de.cb_tipo_dispositivo.currentText()
            entrada = self.ui_de.cb_tipo_entrada.currentText()

            ruta = ''
            if tipo == 'Ratón':
                disp_entrada = Raton(marca=marca, tipoEntrada=entrada)
                ruta = Rutas.RATON
            else:
                disp_entrada = Teclado(tipoEntrada=entrada, marca=marca)
                ruta = Rutas.TECLADO

            if Registro.guardar(disp_entrada, ruta):
                self.ui_de.txt_marca.setText('')
                self.ui_de.stb_estado.showMessage('Ingreso Exitoso', 3000)
            else:
                self.monstrar_mensaje('Dispositivo Entrada', 'Ingrese la marca', QMessageBox.Warning)

        else:
            self.monstrar_mensaje('Dispositivo Entrada', 'Ingrese la marca', QMessageBox.Warning)


    def monstrar_mensaje(self, titulo, mensaje, tipo):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(titulo)
        dlg.setText(mensaje)
        dlg.setIcon(tipo)
        return dlg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = ServicioDispEntradaIngreso()
    application.show()
    sys.exit(app.exec())


