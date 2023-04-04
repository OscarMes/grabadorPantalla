# from datetime import datetime

# tiempo = datetime.now()

# print(tiempo.strftime('%Y:%m:%d, %Y-%m-%d'))

# import pyautogui

# ancho,alto = pyautogui.size()

# tamanoPantalla = (f"{ancho},{alto}")

# print(tamanoPantalla)

#CTRL + K + C


# from pantalla import objPantalla

# #objPantalla.fntConfGrabacion()
# entrada = input("Entra bool")
# objPantalla.fntIniciarGrabacion(bool(entrada))
# entrada = input("Entra bool")
# objPantalla.fntIniciarGrabacion(bool(entrada))
# entrada = input("Entra bool")
# objPantalla.fntIniciarGrabacion(bool(entrada))
# entrada = input("Entra bool")
# objPantalla.fntIniciarGrabacion(bool(entrada))



from PySide2.QtCore import QThread
from prueba2 import objBucle
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from prueba2 import objBucle

class Hilos(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.is_runnig = True

    def run(self):

        while (True):
            objBucle.loop()
            #print("Hola")
        
    def stop(self):
        #self.is_runnig = False
        self.terminate()




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com") 

        pybutton = QPushButton('Click me', self)
        
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(50, 50)  
        self.objHilo = Hilos()   




        pybutton2 = QPushButton('Pausar', self)
        
        pybutton2.clicked.connect(self.Pausar)
        pybutton2.resize(100,32)
        pybutton2.move(80, 80)  
        self.objHilo = Hilos()  
        

    def clickMethod(self):
        self.objHilo.start()
        print('Clicked Pyqt button.')

    def Pausar(self):
        
        self.objHilo.stop()

        print('SE ACABA ESTA VAINA')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )





