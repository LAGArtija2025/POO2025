class A():
    pass

    def saludar(self):
        return "Hola desde A"

class F:
    pass

    def saludar(self):
        return "Hola desde F"

class B(A):
    pass

    def saludar(self):
        return "Hola desde B"

class C(F):
    pass

    def saludar(self):
        return "Hola desde C"

class D(B,C):
    pass

    def saludar(self):
        return "Hola desde D"
    
miObjeto = D()
# print(D.mro())

# print(isinstance(miObjeto, F))
print(issubclass(C,F))
