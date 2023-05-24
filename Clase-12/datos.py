#Ejemplo uso de repositorio
print("Datos personales")
print("-------------------")
nom=str(input("Ingrese su nombre: "))
while True:
    try:
        edad=int(input("Ingrese su edad: "))
        break 
    except:
        print("Valor no corresponde")
print("-----------------------------")
print(f"Su nombre es: {nom} y tiene {edad} años.")

print("Programa finalizado.")