# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\vtn_persona_cargar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vtn_cargar_personas(object):
    def setupUi(self, vtn_cargar_personas):
        vtn_cargar_personas.setObjectName("vtn_cargar_personas")
        vtn_cargar_personas.resize(942, 537)
        self.centralwidget = QtWidgets.QWidget(vtn_cargar_personas)
        self.centralwidget.setObjectName("centralwidget")
        self.tb_personas = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_personas.setGeometry(QtCore.QRect(9, 9, 521, 361))
        self.tb_personas.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tb_personas.setObjectName("tb_personas")
        self.tb_personas.setColumnCount(5)
        self.tb_personas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_personas.setHorizontalHeaderItem(4, item)
        self.txt_idPersona = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_idPersona.setGeometry(QtCore.QRect(630, 40, 113, 20))
        self.txt_idPersona.setObjectName("txt_idPersona")
        vtn_cargar_personas.setCentralWidget(self.centralwidget)
        self.stb_estado = QtWidgets.QStatusBar(vtn_cargar_personas)
        self.stb_estado.setObjectName("stb_estado")
        vtn_cargar_personas.setStatusBar(self.stb_estado)

        self.retranslateUi(vtn_cargar_personas)
        QtCore.QMetaObject.connectSlotsByName(vtn_cargar_personas)

    def retranslateUi(self, vtn_cargar_personas):
        _translate = QtCore.QCoreApplication.translate
        vtn_cargar_personas.setWindowTitle(_translate("vtn_cargar_personas", "Cargar Personas"))
        item = self.tb_personas.horizontalHeaderItem(0)
        item.setText(_translate("vtn_cargar_personas", "Id"))
        item = self.tb_personas.horizontalHeaderItem(1)
        item.setText(_translate("vtn_cargar_personas", "Cedula"))
        item = self.tb_personas.horizontalHeaderItem(2)
        item.setText(_translate("vtn_cargar_personas", "Nombre"))
        item = self.tb_personas.horizontalHeaderItem(3)
        item.setText(_translate("vtn_cargar_personas", "Apellido"))
        item = self.tb_personas.horizontalHeaderItem(4)
        item.setText(_translate("vtn_cargar_personas", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vtn_cargar_personas = QtWidgets.QMainWindow()
    ui = Ui_vtn_cargar_personas()
    ui.setupUi(vtn_cargar_personas)
    vtn_cargar_personas.show()
    sys.exit(app.exec_())