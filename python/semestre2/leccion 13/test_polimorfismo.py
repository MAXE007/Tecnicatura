from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):  #Metodo de polimorfismo
    #print(objeto) #De manera indirecta estamos llamando al str de la Clase Empleado o Gerente
    print(type(objeto)) #Esto es para saber el tipo de dato q recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)
    
empleado = Empleado('Ariel', 50000)
imprimir_detalles(empleado)

gerente = Gerente('Natalia', 60000, 'Sistemas')
imprimir_detalles(gerente)