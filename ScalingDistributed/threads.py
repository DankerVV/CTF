import threading
import time
import datetime


def consultar(id):
    time.sleep(2)

def guardar(id, data):
    time.sleep(5)

tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo_1", target= consultar, args=(1, ))#DEFINIMOS HILO 1
t2 = threading.Thread(name="hilo_2", target= guardar, args=(1,"Adios mundo"))#DEFINIMOS HILO 2

t1.start()#inicia ejecución hilo 1
t2.start()#inicia ejecución hilo 2

#consultar(1)
#guardar(1,"Hola")

t1.join()
t2.join()

tiempo_fin= datetime.datetime.now()
time.sleep(2)

print("Tiempo transcurrido: "+ str(tiempo_fin.second - tiempo_ini.second) + " segundos")
