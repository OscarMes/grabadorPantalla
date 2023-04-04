import os
import sys
from ui_designerGrabador import *
import resources_rc 
from pyqt5_tools import *
from PySide2.QtCore import *
from pantalla import objPantalla


class GrabacionThread(QThread):

    def run(self):
        objPantalla.fntIniciarGrabacion(True)
        while True:
            objPantalla.fntIniciarGrabacion()

    def stop(self):
        self.terminate()




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.btnGrabar.setCheckable(True)
        self.ui.btnGrabar.clicked.connect(self.fntGrabarPantalla)
        self.show()



        self.grabacion_thread = GrabacionThread(self)
        


    def fntGrabarPantalla(self):
        if self.ui.btnGrabar.isChecked():
            self.ui.btnGrabar.setIcon(QIcon('Designer/boton-rec.png'))

            estadoGrabacion = self.grabacion_thread.isRunning()
            self.grabacion_thread.start()
        else:
            self.ui.btnGrabar.setIcon(QIcon('Designer/boton-rec_black.png'))
            
            self.grabacion_thread.stop()
            objPantalla.fntIniciarGrabacion(False)

            print(self.grabacion_thread.isRunning())

                                    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    objHilo = GrabacionThread()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())