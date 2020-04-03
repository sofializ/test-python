def contar_pares(x):
    y=0
    cant_par=0
    while y<=x:
        if y%2==0:
            cant_par+=1
        y+=1
    print(cant_par)

contar_pares(10)
