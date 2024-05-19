import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P1_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.txt_nombre.setReadOnly(True)
        self.txt_pasatiempo.setReadOnly(True)
        self.txt_edad.setReadOnly(True)
        self.txt_tipo_sangre.setReadOnly(True)
        # Área de los Signals
        self.datos = {
            1: ["Lexiss", "Jugar lol", 21, "a+", ":/Team/lex.jpeg"],
            2: ["Rodrigo", "Jugar valo", 21, "a-", ":/Team/rod.jpeg"],
            3: ["Nat", "Hacer stream", 20, "a+", ":/Team/nat.jpeg"],
            4: ["Victor", "Ver peliculas", 20, "a+", ":/Team/yo.jpeg"],
        }

        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

        self.index_control = 0
        self.btn_atras.setEnabled(False)
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datosP = self.datos[self.index_control]
            print(datosP)
            self.btn_adelante.setEnabled(True)
            ##change img
            self.img_persona.setPixmap(QtGui.QPixmap(datosP[-1]))
            self.txt_nombre.setText(datosP[0])
            self.txt_pasatiempo.setText(datosP[1])
            self.txt_edad.setText(str(datosP[2]))
            self.txt_tipo_sangre.setText(datosP[3])

        if self.index_control == 1:
             self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control < 5:
            self.btn_atras.setEnabled(True)
            self.index_control += 1

            datosP = self.datos[self.index_control]
            self.txt_nombre.setText(datosP[0])
            self.txt_pasatiempo.setText(datosP[1])
            self.txt_edad.setText(str(datosP[2]))
            self.txt_tipo_sangre.setText(datosP[3])
            print(datosP)
            ##change img
            self.img_persona.setPixmap(QtGui.QPixmap(datosP[-1]))
        if self.index_control == 4:
             self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

