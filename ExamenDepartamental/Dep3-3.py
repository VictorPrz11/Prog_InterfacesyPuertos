import serial
import sys
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "Dep3-3.ui"  # Nombre del archivo aquí.
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

    def lecturaArduino(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.arduino.inWaiting():
                cadena = self.arduino.readline()
                cadena = cadena.decode()
                cadena = cadena.strip()
                if cadena != " ":
                    self.datos.addItem(cadena)
                    self.datos.setCurrentRow(self.datos.count() - 1)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

