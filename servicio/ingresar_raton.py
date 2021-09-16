import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from datos import Rutas
from datos.RatonDAO import RatonDAO
from datos.Registro import Registro
from dominio.Raton import Raton
from gui.vtn_raton_ingresar import Ui_vtn_raton_ingresar


class ServicioRatonIngreso(QtWidgets.QMainWindow):
    def __init__(self):
        super(ServicioRatonIngreso, self).__init__()
        self.ui = Ui_vtn_raton_ingresar()
        self.ui.setupUi(self)
        self.ui.btn_raton_ingresar.clicked.connect(self.ingresar_raton)




    def  limpiar_formulario(self):
        self.ui.txt_entrada.setText('')
        self.ui.txt_marca.setText('')


    def ingresar_raton(self):
        if self.validar_datos():
            entrada = self.ui.txt_entrada.text().upper()
            marca = self.ui.txt_marca.text().upper()
            cantidad = self.ui.txt_cantidad_botones.text()
            raton = Raton(marca=marca, tipoEntrada=entrada, cantidad_botones=cantidad)
            print(raton)
            if RatonDAO.insertar(raton)==1:
                self.ui.stb_estado.showMessage('Ingreso Exitoso',2000)
                self.limpiar_formulario()

            # if self.monstrar_mensaje('Raton', 'Ingreso Exitoso', QMessageBox.Information) == QMessageBox.Ok:
            #     self.limpiar_formulario()
        else:
            self.monstrar_mensaje('Raton', 'Debe completar todos los datos', QMessageBox.Warning)



    def validar_datos(self):
        if self.ui.txt_marca.text() == '' or self.ui.txt_entrada.text() == '':
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
    application = ServicioRatonIngreso()
    application.show()
    sys.exit(app.exec())