class Persona:
    def __init__(self,nombre,documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__cursos=[]
    def setNombre(self,nombre):
        self.__nombre = nombre
        
    def setDocumento(self,documento):
        self.__documento = documento
        
    def AñadirCursos(self,cursos):
        self.__cursos = cursos
        if cursos not in self.__cursos:
            self.__cursos.append(cursos)
            return self.__cursos
        
    def ConsultarCursos(self):
        return self.__cursos
        
    def getNombre(self):
        return self.__nombre
    
    def getDocumento(self):
        return self.__documento
    
    def ModificarCursos(self,x,y):
        for i in self.__cursos:
            if i==x:
                cursonuevo=self.__cursos.index(i)
                self.__cursos.pop(cursonuevo)
                self.__cursos.insert(cursonuevo,x)
                
    def EliminarCursos(self,x):
        if x in self.__cursos:
            for i in self.__cursos:
                if i == x:
                    self.__curso.remove(i)
        return self.__cursos
#objeto.AñadirCursos('java principiante')
#objeto.AñadirCursos('PYTHON principiante')
