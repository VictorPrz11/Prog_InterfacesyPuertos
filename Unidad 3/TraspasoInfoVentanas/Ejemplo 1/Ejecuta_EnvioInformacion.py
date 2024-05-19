import sys
from PyQt5 import uic, QtWidgets, QtGui
from VentanaSecundaria import MyDialog
qtCreatorFile = "Main_EnvioInfo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sumar)
        # Área de los Signals
    def sumar(self):
        a = int(self.txt_a.text())
        b = int (self.txt_b.text())
        r = a + b
        self.dialogo = MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.txt_resultado.setText(str(r))
        self.dialogo.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())