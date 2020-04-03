def mostrar_primo(x):
    y=1
    div=0
    while(y<=x):
        if x%y==0:
            div+=1
        y+=1
    if div==2:
        print("Es primo")
    else:
        print("No es primo")

mostrar_primo(4)
