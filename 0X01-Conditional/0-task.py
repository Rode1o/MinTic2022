#Leer un número entero y determinar si es un número terminado en 4
x = int(input())
if (x % 10) != 4:
    print("Its not")
else:
    print("It is")