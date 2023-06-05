class futbolista:
    nombre = None
    cantidad_goles = 0
    def _init_(self):
        pass

    def set__Nombre(self,nombre):
        self.nombre = nombre

    def set__cantidad(self, goles):
        self.cantidad_goles = goles
    
    def get_Nombre(self):
        return self.nombre

    def get_goles(self):
        return self.cantidad_goles


James = futbolista()

James.set__Nombre("James")
James.set__cantidad(149)
print(James.get_Nombre())
print(James.get_goles(),"goles anotados")