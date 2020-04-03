def devolver_mayor(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    elif y>z:
        return y
    else:
        return z


print("el mayor es"+str(devolver_mayor(2,1,3)))
print("el mayor es"+str(devolver_mayor(2,3,1)))
print("el mayor es"+str(devolver_mayor(3,2,1)))
