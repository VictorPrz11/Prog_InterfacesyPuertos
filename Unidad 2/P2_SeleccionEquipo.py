import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.cb_lex.toggled.connect(self.sel_lex)
        self.cb_nat.toggled.connect(self.sel_nat)
        self.cb_rodrigo.toggled.connect(self.sel_rodrigo)
        self.cb_victor.toggled.connect(self.sel_victor)

        self.lex = ""
        self.nat = ""
        self.rodrigo = ""
        self.victor = ""

    # Área de los Slots
    def sel_lex(self):
        if self.cb_lex.isChecked():
            print("Lex True")
            self.lex = "LEX\n"
        else:
            print("Lex False")
            self.lex = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.rodrigo + self.victor)
    def sel_nat(self):
        if self.cb_nat.isChecked():
            print("Nat True")
            self.nat = "NAT\n"
        else:
            print("Nat False")
            self.nat = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.rodrigo + self.victor)
    def sel_rodrigo(self):
        if self.cb_rodrigo.isChecked():
            print("Rodrigo True")
            self.rodrigo = "RODRIGO\n"
        else:
            print("Rodrigo False")
            self.rodrigo = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.rodrigo + self.victor)
    def sel_victor(self):
        if self.cb_victor.isChecked():
            print("Victor True")
            self.victor = "VICTOR\n"
        else:
            print("Victor False")
            self.victor = ""
        self.text_equipo.setPlainText(self.lex + self.nat + self.rodrigo + self.victor)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

