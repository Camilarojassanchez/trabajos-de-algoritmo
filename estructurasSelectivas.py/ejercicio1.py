#declaro variables
nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingresar la nota 3: "))

#ue el programa sume nota1nota2nota3
promedioCasi= (nota1) + (nota2) + (nota3)
promedio = promedioCasi/3

#resultado si aprobo el estudiante o no desaprobo
if promedio >= 70:
    print("El estudianto aprobo")
else:
    print("el estudiante desaprobo")
