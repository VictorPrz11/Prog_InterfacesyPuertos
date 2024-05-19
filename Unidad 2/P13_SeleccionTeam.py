
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P13_SeleccionTeam.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.rb_L.clicked.connect(self.clic_lex)
        self.rb_N.clicked.connect(self.clic_nat)
        self.rb_R.clicked.connect(self.clic_rod)
        self.rb_V.clicked.connect(self.clic_yo)


    # Área de los Slots
    def clic_lex(self):
        print("Hiciste clic a lex")
        self.txt_alumno.setText("Lex")
    def clic_nat(self):
        print("Hiciste clic a nat")
        self.txt_alumno.setText("Nat")

    def clic_rod(self):
        print("Hiciste clic a rodrigo")
        self.txt_alumno.setText("Rodrigo")

    def clic_yo(self):
        print("Hiciste clic a Victor")
        self.txt_alumno.setText("Victor")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

