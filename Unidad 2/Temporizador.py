import sys
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Temporizador.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        self.segundoPlano = QtCore.QTimer()
        self.dial.setMinimum(0)
        self.dial.setMaximum(60)
        self.dial.setValue(0)
        self.segundoPlano.timeout.connect(self.contar)
        self.buttonIniciar.clicked.connect(self.iniciar)
        self.dial.valueChanged.connect(self.cambia)
        self.buttonReiniciar.clicked.connect(self.reiniciar)
    def reiniciar(self):
        self.reloj.setText("0")
        self.dial.setValue(0)
        self.segundoPlano.stop()
    def cambia(self):
        self.reloj.setText(str(self.dial.value()))

    def iniciar(self):
        self.num = self.dial.value()
        print(self.num)
        self.segundoPlano.start(500)
        self.cont = self.num


    def contar(self):
        if self.cont <= self.num and self.cont>0:
            self.cont -= 1
            self.dial.setValue(self.dial.value()-1)
            self.reloj.setText(str(self.cont))
        else:
            print("terminado")
            self.segundoPlano.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())