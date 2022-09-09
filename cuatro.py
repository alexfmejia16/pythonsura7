#menu empanadas inteligenctes

contador=0
empanadas=[]
ingredientes=[]
print("1.agregar empanadas ")
print("2.Mostrar empanadas")
print("3. Salir")

while(contador !=3):
    ingredientes=[]
    empanada={}
    contador=int(input("Digite la opcion: "))
    if (contador==1):
        empanada['Nombre']=input("igrese nombre de empanada")
        for i in range (3):
            ingredientes.append(input(f"digite el ingrediente: {i+1}"))

        empanada['ingredientes']=ingredientes
        empanada['precio']=int(input("Ingrese el precio"))
        empanadas.append(empanada)
        print("agregando empanada: ")

    elif(contador==2):
        print("mostrar empanaa")
        print(empanadas)
    elif(contador==3):
        print("salir")
        break

    else:
        print("opcion invalida")
