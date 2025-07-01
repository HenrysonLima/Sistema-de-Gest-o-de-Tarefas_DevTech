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
    def __init__(self, id, descricao, estado, data_inicio, data_fim):
        self.id = id
        self.descricao = descricao

        if estado in ['aberto', 'pendente', 'fechado']:
            self.estado = estado
    
        else:
            print("Estado inválido, por favor insira de novo.")
            self.estado = "aberto"

        self.data_inicio = data_inicio
        self.data_fim = data_fim
    
    def guardar_baseDados(self):
        sql = """
            INSERT INTO tarefas (descricao, estado, data_inicio, data_fim)
            VALUES (%s, %s, %s, %s)
        """
        valores = (self.descricao, self.estado, self.data_inicio, self.data_fim)
        myscursor.execute(sql, valores)
        mydb.commit()

    def alterar_dados(self, nova_descricao, novo_estado, nova_data_inicio, nova_data_fim):
        if novo_estado in ['aberto','pendente','fechado']:
            sql = """
                UPDATE tarefas
                SET descricao = %s, estado = %s, data_inicio = %s, data_fim = %s
                WHERE id = %s
            """
            valores = (nova_descricao, novo_estado, nova_data_inicio, nova_data_fim, self.id)
            myscursor.execute(sql, valores)
            mydb.commit()

            self.descricao = nova_descricao
            self.estado = novo_estado
            self.data_inicio = nova_data_inicio
            self.data_fim = nova_data_fim

            print("Dados alterados com sucesso")
        else: 
            print("Estado inválido. Alteração cancelada.")
            return

from datetime import date

# Criar uma tarefa válida
t1 = Tarefa(
    id=None,  # id pode ser None se for autogerado pelo banco
    descricao="Concluir relatório mensal",
    estado="aberto",
    data_inicio=date(2025, 6, 17),
    data_fim=date(2025, 6, 20)
)

# Guardar na base de dados
t1.guardar_baseDados()
print("Tarefa guardada.")


"""Classe admin"""

class admin:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.privileges = ["add user", "delete user", "ban user"]
        
    def display_info(self):
        print(f"Admin Username: {self.username}")
        print(f"Email: {self.email}")

    def show_privileges(self):
        print(f"{self.username}'s privileges:")
        for privileges in self.privileges:
            print(f"-{privileges}")

    def add_privileges(self, privilege):
        if privilege not in self.privileges:
            self.privileges.append(privilege)
            print(f"Privilege '{privilege}' removed.")
        else:
            print(f"Privilege '{privilege}' not foud.")


"""Classe Grupo"""

class Grupo:
    def __init__(self, turno, membros, tarefa_atual):
        self.turno = turno
        self.membros = membros
        self.tarefa_atual = tarefa_atual
    
    def carregar_do_banco(self, conn):
        with conn.cursor() as cursor:
            # Carrega turno e tarefa_atual do grupo
            cursor.execute("SELECT turno, tarefa_atual FROM grupo WHERE id = %s", (self.id_grupo,))
            row = cursor.fetchone()
            if row:
                self.turno, self.tarefa_atual = row

            cursor.execute("SELECT id_utilizador FROM rel_grupo_utilizadorComum WHERE id_grupo = %s", (self.id_grupo,))
            self.membros = [r[0] for r in cursor.fetchall()]
    
    def salvar_no_banco(self, conn):
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE grupo SET turno = %s, tarefa_atual = %s WHERE id = %s",
                (self.turno, self.tarefa_atual, self.id_grupo)
            )

            cursor.execute("DELETE FROM rel_grupo_utilizadorComum WHERE id_grupo = %s", (self.id_grupo,))

            for id_membro in self.membros:
                cursor.execute(
                    "INSERT INTO rel_grupo_utilizadorComum (id_grupo, id_utilizador) VALUES (%s, %s)",
                    (self.id_grupo, id_membro)
                )

        conn.commit()
    
    def adicionar_membro(self, id_membro):
        if id_membro not in self.membros:
            self.membros.append(id_membro)
    
    def remover_membro(self, id_membro):
        if id_membro in self.membros:
            self.membros.remove(id_membro)


