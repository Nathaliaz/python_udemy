#LISTA: se pueden modificar elementos y estan ordenados
frutas = ['manzana', 'pera', 'kiwi', 'naranja']
# for elementos in frutas:
#     print(elementos)
frutas.append('otro')
frutas.append('pera')
print(frutas)

#TUPLA: No se pueden modificar elementos
frutas = ('manzana', 'pera', 'kiwi')
print(frutas)

#CONJUNTO: Elementos desordenados y se pueden modificar
frutas = {'manzana','pera','kiwi'}
frutas.add('naranja')
frutas.add('pera')
print(frutas)

#DICCIONARIO: Elementos indexados, sin orden y pueden modificarse
frutas = {"apple" :'manazana', "pear" : 'pera', "orange" :'naranja'}
print(frutas)

valor = frutas ["apple"]
print(valor)

print(frutas ["pear"])

frutas ["ginger"] = "jengibre"
print(frutas)

#muestra cada clave y su valor
for valor in frutas.items():
	print(valor)

#verificar que un nuemro este en la lista
lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
print(lista)
numero = 21
if numero in lista:
	print("21 esta en la lista")
else:
	print("21 no esta")