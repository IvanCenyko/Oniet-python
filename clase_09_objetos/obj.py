class Shape (object):
    def areaTotal():
        pass

class Triangle (Shape):
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    def areaTotal(self):
        return self.base * self.altura /2


class Square (Shape):
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    def areaTotal(self):
        return self.base * self.altura


t1 = Triangle(10,10)
s1 = Square(10, 10)

print(s1.areaTotal)