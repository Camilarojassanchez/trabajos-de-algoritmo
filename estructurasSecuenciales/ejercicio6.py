nombre = input("Ingrese el nombre del estudiante: ")

trabajos = float(input("Ingrese la calificación promedio de las actividades :"))
proyectos= float(input("Ingrese la calificación del proyecto final "))
evaluaciones= float(input("Ingrese la calificación promedio de las evaluaciones: "))

nota_Final = (trabajos* 0.8) + (proyectos* 0.3) + (evaluaciones * 0.2)

#resultado

print("La nota final de", nombre, "en algoritmia es:", nota_Final)
