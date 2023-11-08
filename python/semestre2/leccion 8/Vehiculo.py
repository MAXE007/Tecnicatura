class Vehiculo:
    '''
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas
    auto y bicicleta
    '''
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __init__(self):
        return 'Color: '+self.color+', Ruedas: '+ str(self.ruedas)
    
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + ', Velocidad(km/h): '+ str(self.velocidad)
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo
    
    
# Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# Segundo objeto, pero ahora de la clase Auto
auto = Auto('Amarillo', 4, 120)
print(vehiculo)

# Tercer objeto de la clase Bicicleta
bici = Bicicleta('Azul', 2, 'Urbana')
print(bici)