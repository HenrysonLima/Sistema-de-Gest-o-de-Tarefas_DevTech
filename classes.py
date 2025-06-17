import pymysql
from datetime import date 

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "devtech_database",
)

mycursor = mydb.cursor()

""" Class Utilizador"""

class Utilizador:
    
    def __init__(self, nome, turno):
        self.nome = nome
        self.turno = turno

    def mostrarDadosUtilizador(self):
        return f"Nome:{self.nome} | Turno: {self.turno}"
    
    def verDescricaoTarefa(self, tarefa):
        return tarefa.descricao
    
    def mudarEstadoTarefa(self, tarefa, novoEstado):
        estadosValidos = ['Aberto','Pendente','Fechado']
        if novoEstado.lower() in estadosValidos:
            tarefa.estado = novoEstado.lower()
        else:
            raise ValueError("Estado inválido. Os únicos estados são: 'Aberto, 'Pendente' ou 'Fechado'.")
        
    def atribuirDataFimTarefa(self, tarefa, data_fim):
        if isinstance(data_fim, date):
            tarefa.data_fim = data_fim
        else:
            raise TypeError("Erro: O valor introduzido não é uma data válida. Tem de ser ano/mês/dia!")

    def guardar_baseDados(self):
        conexao = ligar_base_dados()
        if conexao:
            # inicia 
            try: 
                cursor = mydb.cursor()
                sql = "INSERT INTO utilizadores (nome, turno) VALUES  (%s, %s)"
                valores = ( self.nome, self.turno)
                cursor.execute(sql, valores)
                mydb.commit()
                cursor.close()
                print("Utilizador guardado com sucesso na base de dados.")
                #usamos o except caso o codigo dê erro
                #MySQLError vem da biblioteca mymsql e é utilizada quando dá erros específicos da base de dados
                # pymysql.MySQLError é o mesmo que fazer from pymysql.err import MySQLError mas depois no except ficaria só except MySQLError as erro 
                except pymysql.MySQLError as erro:
                    print(f"Erro ao guardar utilizador: {erro}")


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

