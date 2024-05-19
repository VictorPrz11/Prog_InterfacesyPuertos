import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P4_Dial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos = {
            1: ["Lexiss", "Jugar lol", 21, "a+", ":/Team/lex.jpeg"],
            2: ["Rodrigo", "Jugar valo", 21, "a-", ":/Team/rod.jpeg"],
            3: ["Nat", "Hacer stream", 20, "a+", ":/Team/nat.jpeg"],
            4: ["Victor", "Ver peliculas", 20, "a+", ":/Team/yo.jpeg"],
        }

        self.dial_team.setMinimum(1)
        self.dial_team.setMaximum(4)
        self.dial_team.setSingleStep(1)
        self.dial_team.setValue(0)
        self.dial_team.valueChanged.connect(self.cambia)
    def cambia(self):
        dataClave = self.dial_team.value()
        print(dataClave)
        imagen = self.datos[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))


    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

