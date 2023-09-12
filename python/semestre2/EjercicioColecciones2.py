#Ejercicio 2: Operaciones de conjuntos con listas
#cree las sig listas en las que no debe haber repeticion

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

#Eliminar los elementos repetidos de ambas listas con conjuntos

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) #union 2 conjuntos
solo1 = list(conjunto1 - conjunto2) #muestra el 1
solo2 = list(conjunto2 - conjunto1) #muestra el 2
interseccion = list(conjunto1 & conjunto2) # ambas

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la 1er lista,pero no la 2da: {solo1}")
print(f"Lista de palabras que aparecen en la 2da lista,pero no la 1ra: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")