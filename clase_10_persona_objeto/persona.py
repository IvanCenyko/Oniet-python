import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

constante_cuil = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

class Persona(object):
    def __init__(self, nombres, apellidos, dni, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
        self.sexo = sexo

    def calcular_cuil(self):
        global constante_cuil
        
        # CUIL final
        cuil = ""
        # lista que voy a usar para calcular el ultimo digito
        calculo_ultimo_digito = []

        # ----------- PRIMEROS DOS DIGITOS ----------
        # si es masculino, primeros dos digitos son 20
        if self.sexo.lower() == 'masculino':
            cuil += '20'
            calculo_ultimo_digito = [2, 0]

        # si es femenino, primeros dos digitos son 27
        elif self.sexo.lower() == 'femenino':
            cuil += 27
            calculo_ultimo_digito = [2, 7]
 
        # ------------- DIGITOS DEL DNI -------------
        # DNI en lista
        dni_en_lista = list(self.dni)


        # para cada digito del dni en lista
        for digito in dni_en_lista:
            # apendo su equivalente en int para cada digito
            calculo_ultimo_digito.append(int(digito))
            # concateno el digito al cuil final
            cuil += digito
        
        # -------------- ULTIMO DIGITO --------------
        suma = 0
        # repito una vez por cada digito
        for i in range(10):
            # sumo => digito constante * digito del cuil
            suma += constante_cuil[i] * int(calculo_ultimo_digito[i])

        # calculo el ultimo digito
        ultimo_digito = 11 - (suma % 11)

        # concateno el ultimo digito
        cuil += str(ultimo_digito)    

        # retorno 
        return cuil

persona = Persona('Iván Ezequiel', "Cenyko", '01234567', 'masculino')
print(persona.calcular_cuil())