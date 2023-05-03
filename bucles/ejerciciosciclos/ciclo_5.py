for i in range(1,1000+1):
    contador=0
    for x in range(1,i+1):
        if i%x==0:
            contador+=1
    if contador==2:
        print(f"el numero no es primo {i}")
    else:
        print(f"el numero es primo {i}")