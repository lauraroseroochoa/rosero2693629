import random

secret_number = int(random.random()*100)
x=0
y=0
while x==y:
    numero= int(input("digita el numero secreto: "))
    if numero==secret_number:
        print("has adivinado el numero")
    if numero != secret_number:
        print("sigue intentando")
        if numero>secret_number:
            print("el numero es menor")
        else:
            print("el numero es mayor")
            

print("has adivinado el numero")