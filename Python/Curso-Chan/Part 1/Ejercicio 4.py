"""
Ejercicio 4: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
def numero_entero_positvo():
    numero_entero_positivo = int(input("Introduzca un numero entero positivo a continuacion: "))

    for i in range(numero_entero_positivo):
        print(i, end=",")
    

numero_entero_positvo()
