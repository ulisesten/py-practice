import sys

from PyQt5 import QtWidgets


from gui.vtn_orden_principal import Ui_vtn_orden_principal
from servicio.ingresar_computador import ServicioComputadorIngreso
from servicio.ingresar_raton import ServicioRatonIngreso
from servicio.ingreso_disp_entrada import ServicioDispEntradaIngreso


class Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        self.ui = Ui_vtn_orden_principal()
        self.ui.setupUi(self)
        self.ui.mni_computador_ingreso.triggered.connect(self.ingresar_computador)
        self.ui.mni_raton_ingreso.triggered.connect(self.ingresar_raton)
        self.ui.mni_disp_entrada_ingresar.triggered.connect(self.ingresar_disp_entrdada)
        self.vtn_computador_ingreso = None
        self.vtn_raton_ingreso = None
        self.vtn_disp_entrada_ingreso = None

    def ingresar_computador(self):
        self.vtn_computador_ingreso = ServicioComputadorIngreso()
        self.vtn_computador_ingreso.show()

    def ingresar_raton(self):
        self.vtn_raton_ingreso = ServicioRatonIngreso()
        self.vtn_raton_ingreso.show()

    def ingresar_disp_entrdada(self):
        self.vtn_disp_entrada_ingreso = ServicioDispEntradaIngreso()
        self.vtn_disp_entrada_ingreso.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Principal()
    application.show()
    sys.exit(app.exec())