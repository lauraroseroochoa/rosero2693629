# ejercicio 4
def is_perfect_number(num):
    sum=0
    for i in range(1,num):
        if num %i ==0:
            sum+=i
    return sum ==num
numeros_perfectos=[]
for i in range(1,1001):
    if is_perfect_number(i):
        numeros_perfectos.append(i)
print("entre los numeros 1 y 1000 estan estos numeros perfectos", numeros_perfectos)