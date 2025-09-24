class A:
    pass

    def saludar(self):
        return "Hola desde A"

class B(A):
    pass

    def saludar(self):
        return "Hola desde B"

class C(A):
    pass

    def saludar(self):
        return "Hola desde C"

class D(B, C):
    pass

    def saludar(self):
        return "Hola desde D"

class E(D):
    pass

    def saludar(self):
        return "Hola desde E"
    
miObjetoE = E()

print(dir(miObjetoE.saludar()))