#from sys import path

#path.append("..\\rosero2693629")

from Book import *
from User import *
from Account import *
#from herenciaAction.tarea_claseUser.Account  import *
objeto1= Book('cien años de soledad','gabriel garcia',452125,'01/05/1967','disponible')

objeto1.AppendDuet('cien años de soledad', 'juan')
print(objeto1.reservationStatus("cien años de soledad"))

objeto1.feedBack('cien años de soledad')

print(objeto1.bookRequest('cien años de soledad'))

print(objeto1.rewnInformation('cien años de soledad'))


laura= Account(1,1,1)
laura= User('laurita', 36)
laura.Verify('laurita', 36)
print(laura.checkAccount('laurita', 36))