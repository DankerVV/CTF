#Gestión de erroes, parte 2, ejemplos
print("\n")
num1=10
num2=2

try:
    print("El resultado de ",num1," ÷ ",num2,"es igual a: ", num1/num2)
    x = int(input("Escribe un numero:"))
    print("Si puedes leer esto, es que no hay error")

except ZeroDivisionError:
    print("Se encontró un error: División entre cero")

except ValueError:
    print("Se encontró un error: El valor ingresado no es un número")

print("El programa continúa con normalidad")

print("\n")


