import pymysql
from datetime import date 
from fpdf import FPDF

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "devtech_database",
)

mycursor = mydb.cursor()

""" Class Utilizador"""

class Utilizador:
    #construtor
    def __init__(self, nome, password, turno):
        self.nome = nome
        self.password = password
        self.turno = turno 

    # método que vai mostrar os dados do utilizador
    def mostrarDadosUtilizador(self):
        return f"Nome:{self.nome} | Turno: {self.turno}"
    
    # método que vai mostrar a descriçãso da tarefa 
    def verDescricaoTarefa(self, tarefa):
        return tarefa.descricao

    # método para mudar o estado da tarefa que o utilizador está a fazer 
    def mudarEstadoTarefa(self, tarefa, novoEstado):
        estadosValidos = ['Aberto','Pendente','Fechado']
        if novoEstado.lower() in estadosValidos:
            tarefa.estado = novoEstado.lower()
        else:
            raise ValueError("Estado inválido. Os únicos estados são: 'Aberto, 'Pendente' ou 'Fechado'.")
        
    # método para guardar os dados do utilizador na base de dados
    def guardar_baseDados(self):
            # vão começar vazios
            conexao = None
            cursor = None
            try:
                conexao = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = "devtech_database",
                )
                #is_connected vai verificar se esta connectado com a base de dados
                if conexao.is_connected():
                    cursor = conexao.cursor() # o cursor vai enviar comandos sql para executar na base de dados    
                    sql = "INSERT INTO t_utilizador(username_utilizador, password_utilizador) VALUES (%s, %s)" # o %s vai ser substituido pelos valores
                    valores = (self.nome, self.turno)
                    cursor.execute(sql, valores) # o cursor vai executar o comando que a variavel sql fez e vai ser alterado pelos valores da variavel valores
                    conexao.commit() # o commit é para confirmar que os dados foram alterados na base de dados
                    print("Utilizador adicionado com sucesso na base de dados.")
            # Se alguma parte do try der erro ele vai buscar e vai mandar uma mensagem de erro com o erro identificado
            #caso o programa crache ele meio que vai ajudar a perceber de onde vem o erri
            except Error as erro: # 
                # vai enviar a mensagem com o erro 
                print("Erro ao guardar o utilizador: {erro}")
            # vai ser excutado mesmo que o try dê erro ou não
            finally:
                #primeiro ele vai fechar a ligação com a base de dados
                # vai verificar se já tem algum valor, caso tenham fecha
                if cursor is not None:
                    cursor.close()
                if conexao is not None:
                    conexao.close() 


"""Classe Tarefa"""

class Tarefa:
    #construtor
    def __init__(self, id, descricao, estado, data_inicio, data_fim):
        self.id = id
        self.descricao = descricao

        # vai verificar se o estado esta com uma destas opções      
        if estado in ['aberto', 'pendente', 'fechado']:
            self.estado = estado # atribui o estado se for entre aquelas opções
        # se não mandar um estado das que foram atribuidas manda uma mensagem de erro e deixa estado em aberto automaticamente
        else:
            print("Estado inválido, por favor insira de novo.")
            self.estado = "aberto"
        
        self.data_inicio = data_inicio # data de inicio da tarefa 
        self.data_fim = data_fim # data de fim 
    # método para guardar as tarefas na base de dados 
    def guardar_baseDados(self):
        #comando sql para inserir na tabela t_tarefas 
        sql = """
            INSERT INTO tarefas (descricao, estado, data_inicio, data_fim)
            VALUES (%s, %s, %s, %s)
        """
        # os %s vão ser mudados pelos valores que forem inseridos 
        valores = (self.descricao, self.estado, self.data_inicio, self.data_fim)
        mycursor.execute(sql, valores) # executa o comando com os valores que são pretendidos 
        mydb.commit() # confirma se dos dados realmente foram inseridos na tabela 

    # método para alterar os dados da tarefa que já exista
    def alterar_dados(self, nova_descricao, novo_estado, nova_data_inicio, nova_data_fim):
        # verifica se o novo estado é válido 
        if novo_estado in ['aberto','pendente','fechado']:
            # comando sql 
            sql = """
                UPDATE tarefas
                SET descricao = %s, estado = %s, data_inicio = %s, data_fim = %s
                WHERE id = %s
            """
            # valores que vão ser substituidos pelos %s no comando sql, incluindo o id da tarefa  para identificar qual será atualizada  
            valores = (nova_descricao, novo_estado, nova_data_inicio, nova_data_fim, self.id)
            mycursor.execute(sql, valores) # executa o comando com os valores que são pretendidos 
            mydb.commit() # confirma se dos dados realmente foram inseridos na tabela 

            # atualiza os atributos do objeto com os novos valores 
            self.descricao = nova_descricao
            self.estado = novo_estado
            self.data_inicio = nova_data_inicio
            self.data_fim = nova_data_fim
            # se der certo manda uma mensagem a confirmar a atualização 
            print("Dados alterados com sucesso")
        else: 
            # caso não tenha dado certo manda uma mensagem de erro 
            print("Estado inválido. Alteração cancelada.")
            return # vai sair da função sem as alterações
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


"""Classe Reuniao"""
class Reuniao:
    def __init__(self, dataDaReuniao, teamLeader, membros, topicosFalados):
        self.dataDaReuniao = dataDaReuniao
        self.teamLeader = teamLeader
        self.membros = membros
        self.topicosFalados = topicosFalados

'''Classe para gerar o relatorio usando a biblioteca FPDF'''
class RelatorioReuniaoPDF(FPDF):
        
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Relatório da Reunião', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

    def adicionar_dados_reuniao(self, reuniao: Reuniao):
        self.set_font('Arial', '', 12)
        
        self.cell(0, 10, f"Data da Reunião: {reuniao.dataDaReuniao}", ln=True)
        self.cell(0, 10, f"Team Leader: {reuniao.teamLeader}", ln=True)

        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "Membros Presentes:", ln=True)
        self.set_font('Arial', '', 12)
        for membro in reuniao.membros:
            self.cell(0, 10, f"- {membro}", ln=True)

        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "Tópicos Falados:", ln=True)
        self.set_font('Arial', '', 12)
        for topico in reuniao.topicosFalados:
            self.multi_cell(0, 10, f"- {topico}")
        
        self.ln(5)

class Admin:
    def __init__(self, nome):
        self.nome = nome
        self.usuarios = {}  # chave: usuario_id, valor: Usuario
        self.configuracoes = {}
        self.reunioes = []

    def criar_usuario(self, usuario_id, nome_usuario):
        if usuario_id in self.usuarios:
            print("Usuário já existe.")
        else:
            self.usuarios[usuario_id] = Usuario(usuario_id, nome_usuario)
            print(f"Usuário '{nome_usuario}' criado com sucesso.")

    def remover_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            nome = self.usuarios.pop(usuario_id).nome
            print(f"Usuário '{nome}' removido.")
        else:
            print("Usuário não encontrado.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("Lista de usuários:")
            for usuario in self.usuarios.values():
                print(usuario)

    def alterar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' alterada para '{valor}'.")

    def ver_configuracoes(self):
        if not self.configuracoes:
            print("Nenhuma configuração definida.")
        else:
            print("Configurações atuais:")
            for chave, valor in self.configuracoes.items():
                print(f"{chave}: {valor}")

    def gerar_relatorio_usuarios(self):
        print(f"Relatório de usuários ({len(self.usuarios)} total):")
        for usuario in self.usuarios.values():
            print(usuario)

    def adicionar_tarefa_usuario(self, usuario_id, tarefa):
        usuario = self.usuarios.get(usuario_id)
        if usuario:
            usuario.adicionar_tarefa(tarefa)
            print(f"Tarefa adicionada ao usuário {usuario.nome}.")
        else:
            print("Usuário não encontrado.")

    def criar_reuniao(self, descricao):
        self.reunioes.append(descricao)
        print(f"Reunião criada: {descricao}")

    def ver_reunioes(self):
        if not self.reunioes:
            print("Nenhuma reunião marcada.")
        else:
            print("Reuniões:")
            for r in self.reunioes:
                print(f"- {r}")

    def definir_turno_usuario(self, usuario_id, turno):
        usuario = self.usuarios.get(usuario_id)
        if usuario:
            usuario.definir_turno(turno)
            print(f"Turno definido para {usuario.nome}.")
        else:
            print("Usuário não encontrado.")

    def alterar_descricao_grupo(self, usuario_id, descricao):
        usuario = self.usuarios.get(usuario_id)
        if usuario:
            usuario.definir_descricao_grupo(descricao)
            print(f"Descrição do grupo atualizada para o usuário {usuario.nome}.")
        else:
            print("Usuário não encontrado.")

    def ver_descricao_grupo_usuario(self, usuario_id):
        usuario = self.usuarios.get(usuario_id)
        if usuario:
            print(f"Descrição do grupo de {usuario.nome}: {usuario.descricao_grupo}")
        else:
            print("Usuário não encontrado.")

    def definir_portavoz(self, usuario_id):
        for uid, usuario in self.usuarios.items():
            usuario.portavoz = False  # Remove qualquer porta-voz anterior
        if usuario_id in self.usuarios:
            self.usuarios[usuario_id].portavoz = True
            print(f"{self.usuarios[usuario_id].nome} agora é o porta-voz do grupo.")
        else:
            print("Usuário não encontrado.")

