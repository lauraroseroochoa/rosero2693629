from sys import path

path.append('..\\modules')
import module
#print(module.counter)
#from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

#import sys

#for p in sys.path:
 #   print(p)