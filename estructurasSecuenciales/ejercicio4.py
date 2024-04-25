total_comisiones= 100

vendedor=str(input("digite su nombre:"))
sueldo=int(input("almacene el sueldo:"))
cantidad = int(input("digite la cantidad de ventas: "))

#resultado
vcomisiones = cantidad*total_comisiones
total=sueldo+vcomisiones
print ("nombre del vendedor:",vendedor,",tiene un sueldo de",sueldo,"durante el mes obtuvo una comision de",cantidad,"valor a pagar es",total,)