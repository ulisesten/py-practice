# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\vtn_orden_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vtn_orden_principal(object):
    def setupUi(self, vtn_orden_principal):
        vtn_orden_principal.setObjectName("vtn_orden_principal")
        vtn_orden_principal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(vtn_orden_principal)
        self.centralwidget.setObjectName("centralwidget")
        vtn_orden_principal.setCentralWidget(self.centralwidget)
        self.mnb_principal = QtWidgets.QMenuBar(vtn_orden_principal)
        self.mnb_principal.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.mnb_principal.setObjectName("mnb_principal")
        self.mnu_Computador = QtWidgets.QMenu(self.mnb_principal)
        self.mnu_Computador.setObjectName("mnu_Computador")
        self.mnu_Monitor = QtWidgets.QMenu(self.mnb_principal)
        self.mnu_Monitor.setObjectName("mnu_Monitor")
        self.mnu_Disp_Entrada = QtWidgets.QMenu(self.mnb_principal)
        self.mnu_Disp_Entrada.setObjectName("mnu_Disp_Entrada")
        self.mnu_Teclado = QtWidgets.QMenu(self.mnu_Disp_Entrada)
        self.mnu_Teclado.setObjectName("mnu_Teclado")
        self.mnu_raton = QtWidgets.QMenu(self.mnu_Disp_Entrada)
        self.mnu_raton.setObjectName("mnu_raton")
        self.mnu_Ayuda = QtWidgets.QMenu(self.mnb_principal)
        self.mnu_Ayuda.setObjectName("mnu_Ayuda")
        vtn_orden_principal.setMenuBar(self.mnb_principal)
        self.stb_estado = QtWidgets.QStatusBar(vtn_orden_principal)
        self.stb_estado.setObjectName("stb_estado")
        vtn_orden_principal.setStatusBar(self.stb_estado)
        self.mni_computador_ingreso = QtWidgets.QAction(vtn_orden_principal)
        self.mni_computador_ingreso.setObjectName("mni_computador_ingreso")
        self.mni_computador_modificar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_computador_modificar.setObjectName("mni_computador_modificar")
        self.mni_computador_eliminar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_computador_eliminar.setObjectName("mni_computador_eliminar")
        self.mni_monitor_ingreso = QtWidgets.QAction(vtn_orden_principal)
        self.mni_monitor_ingreso.setObjectName("mni_monitor_ingreso")
        self.mni_monitor_modificar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_monitor_modificar.setObjectName("mni_monitor_modificar")
        self.mni_monitor_eliminar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_monitor_eliminar.setObjectName("mni_monitor_eliminar")
        self.mni_teclado_ingreso = QtWidgets.QAction(vtn_orden_principal)
        self.mni_teclado_ingreso.setObjectName("mni_teclado_ingreso")
        self.mni_teclado_modificar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_teclado_modificar.setObjectName("mni_teclado_modificar")
        self.mni_teclado_eliminar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_teclado_eliminar.setObjectName("mni_teclado_eliminar")
        self.mni_raton_ingreso = QtWidgets.QAction(vtn_orden_principal)
        self.mni_raton_ingreso.setObjectName("mni_raton_ingreso")
        self.mni_raton_modificar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_raton_modificar.setObjectName("mni_raton_modificar")
        self.mni_raton_eliminar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_raton_eliminar.setObjectName("mni_raton_eliminar")
        self.mni_acerca = QtWidgets.QAction(vtn_orden_principal)
        self.mni_acerca.setObjectName("mni_acerca")
        self.mni_disp_entrada_ingresar = QtWidgets.QAction(vtn_orden_principal)
        self.mni_disp_entrada_ingresar.setObjectName("mni_disp_entrada_ingresar")
        self.mnu_Computador.addAction(self.mni_computador_ingreso)
        self.mnu_Computador.addAction(self.mni_computador_modificar)
        self.mnu_Computador.addAction(self.mni_computador_eliminar)
        self.mnu_Monitor.addAction(self.mni_monitor_ingreso)
        self.mnu_Monitor.addAction(self.mni_monitor_modificar)
        self.mnu_Monitor.addAction(self.mni_monitor_eliminar)
        self.mnu_Teclado.addAction(self.mni_teclado_ingreso)
        self.mnu_Teclado.addAction(self.mni_teclado_modificar)
        self.mnu_Teclado.addAction(self.mni_teclado_eliminar)
        self.mnu_raton.addAction(self.mni_raton_ingreso)
        self.mnu_raton.addAction(self.mni_raton_modificar)
        self.mnu_raton.addAction(self.mni_raton_eliminar)
        self.mnu_Disp_Entrada.addAction(self.mnu_Teclado.menuAction())
        self.mnu_Disp_Entrada.addAction(self.mnu_raton.menuAction())
        self.mnu_Disp_Entrada.addAction(self.mni_disp_entrada_ingresar)
        self.mnu_Ayuda.addAction(self.mni_acerca)
        self.mnb_principal.addAction(self.mnu_Computador.menuAction())
        self.mnb_principal.addAction(self.mnu_Monitor.menuAction())
        self.mnb_principal.addAction(self.mnu_Disp_Entrada.menuAction())
        self.mnb_principal.addAction(self.mnu_Ayuda.menuAction())

        self.retranslateUi(vtn_orden_principal)
        QtCore.QMetaObject.connectSlotsByName(vtn_orden_principal)

    def retranslateUi(self, vtn_orden_principal):
        _translate = QtCore.QCoreApplication.translate
        vtn_orden_principal.setWindowTitle(_translate("vtn_orden_principal", "Administración de Ordenes"))
        self.mnu_Computador.setTitle(_translate("vtn_orden_principal", "Computador"))
        self.mnu_Monitor.setTitle(_translate("vtn_orden_principal", "Monitor"))
        self.mnu_Disp_Entrada.setTitle(_translate("vtn_orden_principal", "Disp. Entrada"))
        self.mnu_Teclado.setTitle(_translate("vtn_orden_principal", "Teclado"))
        self.mnu_raton.setTitle(_translate("vtn_orden_principal", "Ratón"))
        self.mnu_Ayuda.setTitle(_translate("vtn_orden_principal", "Ayuda"))
        self.mni_computador_ingreso.setText(_translate("vtn_orden_principal", "Ingresar"))
        self.mni_computador_modificar.setText(_translate("vtn_orden_principal", "Modificar"))
        self.mni_computador_eliminar.setText(_translate("vtn_orden_principal", "Eliminar"))
        self.mni_monitor_ingreso.setText(_translate("vtn_orden_principal", "Ingreso"))
        self.mni_monitor_modificar.setText(_translate("vtn_orden_principal", "Modificar"))
        self.mni_monitor_eliminar.setText(_translate("vtn_orden_principal", "Eliminar"))
        self.mni_teclado_ingreso.setText(_translate("vtn_orden_principal", "Ingresar"))
        self.mni_teclado_modificar.setText(_translate("vtn_orden_principal", "Modificar"))
        self.mni_teclado_eliminar.setText(_translate("vtn_orden_principal", "Eliminar"))
        self.mni_raton_ingreso.setText(_translate("vtn_orden_principal", "Ingresar"))
        self.mni_raton_modificar.setText(_translate("vtn_orden_principal", "Modificar"))
        self.mni_raton_eliminar.setText(_translate("vtn_orden_principal", "Eliminar"))
        self.mni_acerca.setText(_translate("vtn_orden_principal", "Acerca"))
        self.mni_disp_entrada_ingresar.setText(_translate("vtn_orden_principal", "Ingresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vtn_orden_principal = QtWidgets.QMainWindow()
    ui = Ui_vtn_orden_principal()
    ui.setupUi(vtn_orden_principal)
    vtn_orden_principal.show()
    sys.exit(app.exec_())