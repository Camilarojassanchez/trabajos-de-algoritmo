#declarar variables
edad_meses = float(input(" introduce tu edad en meses: "))
nivel_hemoglobina = float(input("introduce tu nivel de hemoglobina en g%: "))
sexo = input( introduce tu sexo (femenino/masculino): ")

#decision si tiene anemia o no  y si, si imprime que es positivo  y si no es negativo
if edad_meses <= 1:
    rango = (13, 26)
elif edad_meses <= 6:
    rango = (10, 18)
elif edad_meses <= 12:
    rango = (11, 15)
elif edad_meses <= 60:
    rango = (11.5, 15)
elif edad_meses <= 120:
    rango = (12.6, 15.5)
elif edad_meses <= 180:
    rango = (13, 15.5)
elif sexo.lower() == 'femenino':
    rango = (12, 16)
elif sexo.lower() == 'masculino':
    rango = (14, 18)
else:
    print ("introduce un sexo válido: 'femenino' o 'masculino'.")

#resultado de hemglbina
if nivel_hemoglobina < rango[0]:
    print ("Positivo para anemia")
else:
    print ("Negativo para anemia")