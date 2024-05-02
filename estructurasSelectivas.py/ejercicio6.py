# programa para estimular a los almunos 
from random import * 
Nom_alumno=str(input("ingrese el nombre del estudiante: "))

#declaro otra variable
Prom_Alumno=int(input("ingrese el promedio del estudiante en el ultimo perido: ")) 

if Prom_Alumno>=9: 

# impirmo el decuento obtenido por el alumno deacuerdo con el promedio 
    print("te toco un descuento del 30%")
    Pension=float(input("ingrese el pago de la pension: "))

     # declaro el valor a pagar 
    Valor_Pagar=Pension-(Pension*0.30) 
    print (f"el total a pagar es: {Valor_Pagar}") 
elif Prom_Alumno<9: 
    print("no te toco decuento") 
    Pension=float(input("ingrese el pago de la pension: ")) 
    IVA=0.10 

#decalro el valor a pagar es igual a la pension sumada con el apension del alumno
    Valor_Pagar=Pension+(Pension*IVA) 

    #resultado total a pagar con el IVA
    print (f"el total a pagar es: {Valor_Pagar} Con el IVA del 10%") 