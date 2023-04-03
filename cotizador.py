# el cotizador es una compilacion de los temas que se han estudiado, TIPOS DE DATOS OPERADORES INPUT PRINT

print("HOLA SOY MASHA.... \nAsistente de Global Cargo \nTe voy ayudar con tu cotizacion de impuestos")

# variables e ingreso de datos proporcionados por el cliente.
nombre = str(input("Dime cual es tu nombre: "))
detalle = str(input("Que producto vas a traer: "))
valor = float(input("Cuanto te costo. Utiliza el punto para decimales: "))

print(f"Gracias {nombre} por los datos, en un moento tendras los datos... ")

# Constantes de la logica del proceso
iva = 0.12
fondinfa = 0.005

# calculo de impuestos
ivaCalculo = round(float(valor * iva), 2)
fondinfaCalculo = round(float((valor + iva) * fondinfa), 2)
totalImpuestos = ivaCalculo + fondinfaCalculo

print("AQUI TINES: ")
print(f"El iva: ${ivaCalculo} \nEl fondinfa: ${fondinfaCalculo} \nEl impuestos totales hasta aqui: ${totalImpuestos}")

