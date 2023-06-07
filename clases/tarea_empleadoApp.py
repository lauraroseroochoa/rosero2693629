from tarea_empleado import *

#print(Empleado.contador)
print(Empleado.contador)
empleado1=Empleado('juan','empleadojefe',1000000)
empleado2=Empleado('laura','gerente',2000000)
empleado3=Empleado('fgg','fgf',400000)
print(Empleado.contador)
empleado1.setSalario(1000000)
print(empleado1.getSalario(1000000))
print(empleado1.salarioHora())
print(empleado1.__dict__,empleado1.contador)
print(empleado2.__dict__,empleado2.contador)

print(empleado1.salarioIPC(salario))
print(empleado2.calcularExtras(salario))
print(Empleado.contador)