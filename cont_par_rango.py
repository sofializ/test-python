def contar_pares_rango(x,y):
    i=x
    f=y
    cant_par=0
    while(i<=f):
        if i%2==0:
            cant_par+=1
        i+=1
    print(cant_par)
contar_pares_rango(-2,4)
