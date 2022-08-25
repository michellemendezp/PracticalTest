"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

a = int(input("¿Cuál es tu edad? "))
for i in range(a):
    print("Has cumplido " + str(i+1) + " años")