colores = ["rojo", "verde", "azul"]
for color in colores:
	print(color)

range (8)
for numero in range(8):
	print(numero)

for numero in range(3,8):
	print(numero)

colores = ["rojo", "verde", "azul"]
for color in colores:
	print(color)

#terminar al llegar al 5
for numero in range (10):
	if numero == 5:
		break
	print(numero)


#WHILE: ejecutar un conjunto de acciones mientras sea true la condicion -- bucle
valor = 10
fin = 20
while valor < fin:
	print(valor)
	valor = valor +1