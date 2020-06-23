class usuario:
    def __init__(self, nombre, edad, genero, dni):
        self.nombre= nombre
        self.edad = edad
        self.genero  = genero
        self.dni = dni

usuario1 = usuario('Luciana', '25', 'Femenino', '22.333.444')
print(usuario1.nombre)