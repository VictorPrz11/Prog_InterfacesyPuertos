import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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

        self.combo_team.addItem("Selecciona...", 0)
        self.combo_team.addItem("Lex", 1)
        self.combo_team.addItem("Rodrigo", 2)
        self.combo_team.addItem("Nat", 3)
        self.combo_team.addItem("Victor", 4)

        self.combo_team.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        try:
            print("Text: " + self.combo_team.currentText())
            print("Index: " + str(self.combo_team.currentIndex()))
            print("Data: " + str(self.combo_team.currentData()))

            dataClave = self.combo_team.currentData()
            imagen = self.datos[dataClave][-1]
            self.img_persona.setPixmap(QtGui.QPixmap(imagen))

        except Exception as e:
            print(e)



    # Área de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


