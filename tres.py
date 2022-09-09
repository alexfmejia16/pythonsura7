#Crear un menu de dos opciones 
contador=0
print("Enamorate de Antioquia")
print("Menu")
print("1. Agregar pueblos")
print("2. Mostrar Rutas ")
print("3. Sali")
pueblos=[]
while (contador !=3):
    pueblo={}
    contador = int(input("Digita una opcion"))
    if(contador==1):
        print("Agregando pueblo:")
        pueblo['nombre']= input("ingrese el nombre del pueblo")
        pueblo['distancia']= int(input("ingrese la distancia del pueblo"))
        pueblo['poblacion']= int(input("igrese la poblacion"))
        pueblos.append(pueblo)

    elif(contador==2):
        print("Mostrando rutas:")
        print(pueblos)
    elif(contador==3):
        print("Saliendo:")
        break
    else:
        print("Opcion Invalda:")