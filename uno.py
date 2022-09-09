#variables con elemento del mismo tipo 
#Lista de los numeros pares 

numerosPares =[]

#generar un ciclo while que de 10 vueltas

contador = 0
while (contador < 10):
    numero = (int (input("Digite un numero par: ")))
    if (numero % 2==0):
        numerosPares.append(numero)
        contador = contador+1
    
for observador in numerosPares:
    print(observador)
