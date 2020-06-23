#creo un diccionario
frutas = {"apple" :'manazana', "pear" : 'pera', "orange" :'naranja',"lemon": "limon"}
print(frutas)

#muestro traduccion de la palabra orange
print(frutas ["orange"])

#agrego elemento
frutas ["pineapple"] = "piña"
print(frutas)

#Bucle para mostrar todos los elementos
for valor in frutas:
	print(valor)

for clave,valor in frutas.items():
	print("{} significa {}" .format(clave,valor))


