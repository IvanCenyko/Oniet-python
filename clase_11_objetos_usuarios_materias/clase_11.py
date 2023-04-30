class Alumno(object): #clase
    def __init__(self, nombre, DoB, matr): #atributos
        self.nombre = nombre
        self.DoB = DoB
        self.matr = matr
        self.materias = []

    def poner(self, materia):   #metodo
        if not materia in self.materias:
            self.materias.append(materia)
    def sacar(self, materia):
        for i in(self.materias):
            if i == materia:
                self.materias.remove(materia)

        
Messi = Alumno("Lionel Messi", "9/12/18", "912") #objeto
Messi.poner("Fulbo")
print(Messi.materias)
Messi.sacar("Fulbo")
print(Messi.materias)