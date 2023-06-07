#Escriba una clase Empleado que tenga como propiedades
#Nombre, cargo, salario
#Escriba metodos contructores, setters y getters
#Escriba un método que permita calcular cuanto gana el empleado en una hora
#Un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
#Un método que reciba una cantidad de horas extras y calcule el salario incrementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide

#Anexar variable de clase que cuente cantidad de objetos creados de esa clase

class Empleado:

    contador=0
    
    def __init__(self,nombre:str,cargo:str,salario:int):
        Empleado.contador+=1
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

    def setNombre(self,nombre):
        self.__nombre=nombre

    def setCargo(self,cargo):
        self.__cargo=cargo

    def setSalario(self,salario):
        self.__salario=salario

    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSalario(self):
        return self.__salario
    
    def salarioHora(self,salario):
        self.__salario=salario
        s=salario/4
        d=s/5
        h=d/8
        x=h
        return int(x)
    def salarioIPC(self,salario):
        self.__salario=salario
        ipc=0.1312
        incremento=0
        if salario==1160000:
            salario2=salario*ipc
            totalsalario=salario2+salario
            incremento=totalsalario*0.03
            totalsalario2=incremento+salario
            return int(totalsalario2)

        else:
            salario2=salario*ipc
            totalsalario=salario2+salario
            return int(totalsalario)

    def calcularExtras(self,salario):
        self.__salario=salario
        extras=int(input('ingrese el numero de horas extras realizadas en el mes recuerda maximo dos diarias: '))
        if extras <=40:
            horaextra=Empleado.salarioHora(self,salario)*0.25
            valorextra=horaextra+ Empleado.salarioHora(self,salario)
            incrementoextras=valorextra*extras+salario
            return int(incrementoextras)
        else:
            print(' no se permiten mas de dos horas diarias')
print(Empleado.contador)
empleado1=Empleado('juan','empleado',1000000)
empleado2=Empleado('laura','gerente',2000000)
empleado3=Empleado('paula','coordinadora',400000)
#print(Empleado.contador)
empleado1.setNombre('pepito')
empleado1.setCargo('subdirector')
empleado1.setSalario(1600000)

#print(empleado1.getSalario(1000000))
print(f'en una hora gana{empleado1.salarioHora(1600000)}')
print(empleado1.__dict__,empleado1.contador)
print(empleado2.__dict__,empleado2.contador)

print(empleado1.getNombre())
print(empleado1.getCargo())
print(empleado1.getSalario())


print(f'incremento salarial con el IPC: {empleado1.salarioIPC(1600000)}')
print(f'tu salario mas las horas extras es:{empleado1.calcularExtras(1600000)}')
print(f'numeero de objetos instanciados{Empleado.contador}')