from tkinter import END, messagebox
import tkinter as tk
import math
import time
import os
#HOLA MUNDO CON INTERFAZ
tiempo = 0

root = tk.Tk()
root.title("FORMULARIO")
root.config(width=600, height=600)

#INGRESA TU NOMBRE
tk.Label(root, text="NOMBRE: ").place(x=20,y=70)
txtNombre=tk.Entry()
txtNombre.place(x=100,y=70)

#INGRESA TU APELIIDO
tk.Label(root, text="APELLIDOS: ").place(x=20,y=120)
txtApellido=tk.Entry()
txtApellido.place(x=100,y=120)

#INGRESA TU EDAD
tk.Label(root, text="EDAD: ").place(x=20,y=170)
spinbox = tk.Spinbox(root, from_=0, to=150, increment=1, width=3)
spinbox.place(x=100,y=170)

#INGRESA TU PAIS
tk.Label(root, text="PAÍS DE RESIDENCIA: ").place(x=20,y=220)
txtPais=tk.Entry()
txtPais.place(x=160,y=220)

#Temporizador
# Función para actualizar el contador de segundos
def actualizar_contador():
    segundos_transcurridos = int(time.time() - tiempo_inicio)
    tiempo = segundos_transcurridos
    print(segundos_transcurridos)
    root.after(1000, actualizar_contador)  # Actualizar cada 1000 ms (1 segundo)
    #GUARDAR CADA 5 SEGUNDOS
    if((segundos_transcurridos%3)==0) and (segundos_transcurridos>0):
        print("A guardar")
        guardar()

# Iniciar el tiempo
tiempo_inicio = time.time()
# Llamar a la función de actualización inicial
actualizar_contador()

#FUNCION DE GUARDADO
def guardar():
    with open('restaurar.txt', 'w') as archivo:
        archivo.write(txtNombre.get()+"\n")
        archivo.write(txtApellido.get()+"\n")
        archivo.write(spinbox.get()+"\n")
        archivo.write(txtPais.get())

#FUNCION RESTAURAR
def restaurar():
    print("RESTAURANDO")
    txtNombre.insert(0,lineas[0])
    txtApellido.insert(0,lineas[1])
    spinbox.delete(0,tk.END)
    spinbox.insert(0,lineas[2])
    txtPais.insert(0,lineas[3])

#ABRIR ARCHIVO Y TOMAR LOS DATOS
if(tiempo==0):
    with open('restaurar.txt', 'r') as archivo:
        lineas = archivo.readlines()
        print(lineas)
        if(len(lineas)==4):
            restaurar()

root.mainloop()