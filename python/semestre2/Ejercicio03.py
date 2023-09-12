# Ejercicio 3: Insertar elementos y ordenarlos

lista = []
salir = False
while not salir:
    numero = int(input('Escriba un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()    #Ordena la lista
print(f'\nLista ordenada: \n{lista}')