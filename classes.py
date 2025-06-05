import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "devtech_database"
)
myscursor  = mydb.cursor()

""" Class Utilizador"""

class Utilizador:
    
    def __init__(self, nome, turno):
        self.nome = nome
        self.turno = turno

    def teste(self):
        return "Meu nome é", self.nome, "e o meu turno é", self.turno
        

objeto = Utilizador("Nicole", "Noite")

print(objeto.teste())


"""Classe Tarefa"""

class Tarefa:
    def __init__(self, descricao, estado, data_inicio, data_fim):
        self.descricao = descricao

        if estado in ['aberto', 'pendente', 'fechado']:
            self.estado = estado
    
        else:
            print("Estado inválido, por favor insira de novo.")
            return

        self.data_inicio = data_inicio
        self.data_fim = data_fim
