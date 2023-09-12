#Ejercicio 1: Eliminar duplicados de una lista

lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1,"Ariel", 2, "Alberto"]
#conjunto = set(lista) #Convertimos lista en un set
#lista = list(conjunto) #Convertimos conjunto a lista
lista = list(set(lista)) #Conversion echa en 1 sola linea de codigo
print(lista)