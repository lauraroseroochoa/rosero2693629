from tarea_empleado import *

print(Empleado.contador)
empleado1=Empleado('juan','empleado',1000000)
empleado2=Empleado('laura','gerente',2000000)
empleado3=Empleado('paula','coordinadora',400000)
#print(Empleado.contador)
empleado1.setNombre('pepito')
empleado1.setCargo('subdirector')
empleado1.setSalario(1600000)

#print(empleado1.getSalario(1000000))
print(f'en una hora gana: {empleado1.salarioHora(1600000)}')
print(empleado1.__dict__,empleado1.contador)
print(empleado2.__dict__,empleado2.contador)

print(empleado1.getNombre())
print(empleado1.getCargo())
print(empleado1.getSalario())


print(f'incremento salarial con el IPC: {empleado1.salarioIPC(1600000)}')
print(f'tu salario mas las horas extras es: {empleado1.calcularExtras(1600000)}')
print(f'numero de objetos instanciados {Empleado.contador}')