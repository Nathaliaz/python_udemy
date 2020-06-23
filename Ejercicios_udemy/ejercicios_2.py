numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8
# compara 2 expresiones true
(numero1 > numero2) and (numero3 < numero4)
print((numero1 > numero2) and (numero3 < numero4))

# compara 2 expresiones diferentes
(numero1 > numero2) and (numero3 > numero4)
print((numero1 > numero2) and (numero3 > numero4))

# toma una expresion u otra
(numero1 > numero2) or (numero3 > numero4)
print((numero1 > numero2) or (numero3 > numero4))

# OTRAS: agregar 1 elemento
frutas1 = ['manzana', 'pera', 'naranja']
frutas1.append('kiwi')
print(frutas1)
#muestra cantidad de elementos
len (frutas1)
print(len (frutas1))


frutas2 = 'banana'
#verificar si una variable esta en otra variable
frutas2 is not frutas1
print(frutas2 is not frutas1)
