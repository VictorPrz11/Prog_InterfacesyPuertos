import serial
import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P13_InterfazConexionArduino.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.onoff = 0
        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)

        self.arduino = None
        self.btn_encender.clicked.connect(self.encenderApagarLed)

    #Area de Slots
    def accion(self):
       try:
           texto_boton = self.btn_accion.text()
           com = self.txt_com.text()
           if texto_boton == "CONECTAR" and self.arduino is None:
               self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
               self.btn_accion.setText("DESCONECTAR")

               self.txt_estado.setText("CONECTADO")
           elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
               self.arduino.close()
               self.btn_accion.setText("RECONECTAR")
               self.txt_estado.setText("DESCONECTADO")
           else:
               self.arduino.open()
               self.btn_accion.setText("DESCONECTAR")

               self.txt_estado.setText("CONECTADO")
       except Exception as e:
        print(e)


    def encenderApagarLed(self):

        if not self.arduino is None and self.arduino.isOpen():
            if(self.onoff == 0):
                self.btn_encender.setText("APAGAR")
                self.onoff = 1
            else:
                self.onoff = 0
                self.btn_encender.setText("ENCENDER")
            self.arduino.write(str(self.onoff).encode())
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

