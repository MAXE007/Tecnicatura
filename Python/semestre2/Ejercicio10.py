#Ejercicio 10: no repetir caracteres
# Hacer programa que pida una cadena por teclado
#luego meter los caracteres en una lista sin repetir
cadena = input('Escriba una cadena: ')
lista = []
for i in cadena:
    if i not in lista: #Si el caracter aun no esta en la lista
        lista.append(i) #lo agregamos a la lista
print(f'\nLista de caracteres sin repetir ninguno: \n {lista}')