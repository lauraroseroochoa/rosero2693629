#from sys import path

#path.append("..\\rosero2693629")

from Book import *
from User import *
from Account import *
#from herenciaAction.tarea_claseUser.Account  import *
obejto1= Book('cien años de soledad','jj',452125,'45/528/585','disponible')

obejto1.AppendDuet('cien años de soledad', 'jjaj')
print(obejto1.reservationStatus("cien años de soledad"))

#obejto1.feedBack('cien años de soledad')

#print(obejto1.bookRequest('hhh'))

#print(obejto1.rewnInformation('cien años de soledad'))


laura= Account(1,1,1)
laura= User('laurita', 36)
laura.Verify('laurita', 36)
print(laura.checkAccount('laurita', 36))