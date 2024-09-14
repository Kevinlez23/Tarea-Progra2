Año = int(input("ingrese el año para saber si es bisiesto: "))

if Año>=1500 and Año<=2030:
    def bisiesto(Año):    
        if Año%4==0 and Año%100!=0: 
            return True
        elif Año%100==0 and Año%400== 0:
            return True
        else:
            return False
    print(bisiesto(Año))
else: 
    print("solo se permiten años de 1500 a 2030")