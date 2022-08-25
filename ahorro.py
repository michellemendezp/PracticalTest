producto = input("Que compraras")
precio = float(input("Coloca el precio de lo que compraras"))
ahorroActual = 0

while precio > ahorroActual:
    mesada = float(input("Coloca tu mesada"))
    ahorroActual = ahorroActual + mesada
    restante = precio - ahorroActual
    tiempoTotal = precio / mesada
    tiempoActual = ahorroActual / mesada
    tiempoRestante = tiempoTotal - tiempoActual
    print ("Actualmente tienes ahorrado:", ahorroActual) 
    print ("El dinero que te falta es $:", restante) 
    print ("los meses para cumplir la meta:", tiempoRestante) 
print ("Felicidades ya llegaste a la meta:", producto)      

