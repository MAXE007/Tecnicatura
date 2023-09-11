print(nombres[ :3])#Indices a mostrar 0,1,2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificar un valor dentro de nuestra lista
nombres[2]='Liliana'
nombres[0]='Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista ')
#Preguntamos cuantos elementos tiene
print(len(nombre)) # le pasamos como parametro la lista
