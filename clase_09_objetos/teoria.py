class Auto(object): #clase
    def __init__(self, cambio, combustible, velocidad_maxima):
        self.cambio = cambio #atributo
        self.combustible = combustible #atributo
        self.velocidad_maxima = velocidad_maxima #atributo

    def hacer_cambio(self, cambio): #metodo
        self.cambio = cambio
    
    def medidor_combustible(self): #metodo
        return self.combustible


#objeto
mi_auto = Auto(1, 100, 120)
mi_auto.hacer_cambio(3)
print(mi_auto.cambio)
