import cv2
import numpy as np
import pyautogui
import time
from datetime import datetime

import time

class Pantalla:
    def __init__(self):
        self.ancho,self.alto = pyautogui.size() 
        self.tamanoPantalla = (self.ancho,self.alto)


    def fntConfGrabacion(self):
        formato = "XVID"
        self.fps = 30
        prev = 0

        nombreVideo = datetime.now() 
        self.strtiempo = nombreVideo.strftime('%H-%M-%S, %m-%Y')+(".avi")


        self.salidaFormato = cv2.VideoWriter_fourcc(*'XVID')
        

    def fntIniciarGrabacion(self, grabando):
        self.fntConfGrabacion()
        if grabando == True:
            self.salidaVideo =cv2.VideoWriter(self.strtiempo,self.salidaFormato,20.0,(self.tamanoPantalla))
            print(grabando)
        while grabando == True:
            
            start = time.time()
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.salidaVideo.write(frame)

            # Calcular el tiempo que tardó en capturar la pantalla y escribir el frame en el archivo de video
            elapsed = time.time() - start

            # Si el tiempo transcurrido es menor que el tiempo entre frames (1/fps),
            # dormir durante el tiempo restante para igualar la velocidad de la grabación a la velocidad en tiempo real
            if elapsed < 1/self.fps:
                time.sleep(1/self.fps - elapsed)

            if grabando != True:
                break

        cv2.destroyAllWindows()
        self.salidaVideo.release()

objPantalla = Pantalla()