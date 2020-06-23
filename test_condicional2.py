nota = int(input("Introduce una nota:  "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")