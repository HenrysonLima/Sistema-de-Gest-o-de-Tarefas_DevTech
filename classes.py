""" Class Utilizador"""

class Utilizador:
    
    def __init__(self, nome, turno):
        self.nome = nome
        self.turno = turno

    def teste(self):
        return "Meu nome é", self.nome, "e o meu turno é", self.turno
        

objeto = Utilizador("Nicole", "Noite")

print(objeto.teste())

