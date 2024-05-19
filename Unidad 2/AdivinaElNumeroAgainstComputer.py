import sys
from PyQt5 import uic, QtWidgets, QtCore
import random
qtCreatorFile = "AdivinaElNumero.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.segundoPlano = QtCore.QTimer(self)
        self.numeroMaquina = 0
        self.numeroUsuario = 0
        self.setNumber.clicked.connect(self.iniciaJuego)
    def iniciaJuego(self):
        if(self.setNumber.text() == 'Set'):
            self.numeroUsuario = int(self.IngresoJugador.text())
            self.IngresoJugador.clear()
            self.setNumber.setText('Adivinar')
            self.Instrucciones.setText('Adivina el numero de la maquina')
            self.numeroMaquina = random.randint(0, 100)
            print(self.numeroUsuario)
        elif(self.setNumber.text() == 'Adivinar'):
            jugador = int(self.IngresoJugador.text())
            if(self.numeroMaquina == jugador):
                self.Ganador.setText('GANASTE!!')
            elif(self.numeroMaquina != self.IngresoJugador.text()):
                self.Instrucciones.setText('Turno maquina')
                self.segundoPlano.singleShot(1000, self.turnoMaquina)
    def turnoMaquina(self):
            turnoMaquina = random.randint(0, 100)
            print(f'Número de la máquina: {self.numeroMaquina}')
            if turnoMaquina == self.numeroUsuario:
                self.Ganador.setText('¡PERDISTE!')
            self.Instrucciones.setText('Adivina el número de la máquina')
    def reinicio(self):
        if(self.Instrucciones.text() == 'GANASTE!!'):
            pass
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())