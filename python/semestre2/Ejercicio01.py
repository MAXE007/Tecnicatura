#Ejercicio 1: Llenar una lista y luego mostrar con el bucle for.

#lista = []
#i = 1
#while i <= 50:
#    lista.append(i)
#    i += 1
lista = list(range(1, 51)) # Algoritmo eficaz
for i in lista:
    print(i,end='-')
