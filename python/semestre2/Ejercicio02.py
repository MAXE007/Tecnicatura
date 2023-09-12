# Ejercicio 2: Modificar los elementos de una lista
lista = list(range(1, 11))
print('Lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar: '))
#Multiplicamos todos los elementos de una lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')