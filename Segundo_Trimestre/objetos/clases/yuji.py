class EquipoVoleibol:
    nombre: None
    edad=0
    salto=0.0
    def __init__(self):
        pass
    def set__nombre(self,nombre):
        self.nombre = nombre
    
    def set__edad(self,edad):
        self.edad = edad
        
    def set__salto(self,salto):
        self.salto = salto
        
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_salto(self):
        return self.salto
    
    nishida= EquipoVoleibol()
    nishida.set__nombre('nishida')
    nishida.set__edad(23)
    nishida.set__salto(3.46)
    print(nishida.get_nombre())
    print(nishida.get_edad(),'años')
    print(nishida.get_salto(),'cm')