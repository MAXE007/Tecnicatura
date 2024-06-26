class Producto:
    contador_productos = 0 #Variable de clase
    
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #Aumento para la variable clase
        self._id_producto = Producto.contador_productos #Asignacion desde la variable de clase
        self._nombre = nombre
        self._precio = precio
    #Metodos setter and getters
    @property
    def nombre(self):
        self._nombre = nombre
        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio
     
    #Sobre escribimos el metodo srt    
    def __str__(self):
        return f'Id producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'
    
if __name__ == '__main__':  #La prueba se ejecuta desde aca
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)