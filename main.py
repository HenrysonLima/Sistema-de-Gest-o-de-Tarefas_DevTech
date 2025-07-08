from classes import RelatorioReuniaoPDF, Reuniao #adicionar sua classe

def GerarRelatorioDeReuniao():
    dataReuniao = input("Insira a data da reunião: ")
    teamLeader = input("Nome do TeamLeader: ")
    listaDeMembros = []

    while True:
        print("\nMembros\n")
        membro = input("Insira o nome de um participante \ndigite <sair> se já tiver adicionado todos: ")
        print("\n")
        stringEmMinusculo = membro.lower()
        if stringEmMinusculo == "sair":
            break
        listaDeMembros.append(membro)

    listaDeTopicosFalados = []
    while True:
        print("\nTópicos falados\n")
        topicoFalado = input("Insira um tópico falado na reunião \ndigite <sair> se já tiver inserido todos: ")
        print("\n")
        stringEmMinusculo = topicoFalado.lower()
        if stringEmMinusculo == "sair":
            break
        listaDeTopicosFalados.append(topicoFalado)

    objetoReuniao = Reuniao(dataReuniao, teamLeader, listaDeMembros, listaDeTopicosFalados)

    #código para geraar relatorio pdf
    pdf = RelatorioReuniaoPDF()
    pdf.add_page()
    pdf.adicionar_dados_reuniao(objetoReuniao)

    #nome do ficheiro pdf com a data da reuniao
    dataReuniao = dataReuniao.replace("/", "-")
    nomeDoFicheiro = f"relatorio_reuniao_{dataReuniao}.pdf"
    pdf.output(nomeDoFicheiro)

GerarRelatorioDeReuniao() #Função para ser chamada quando o admin quiser gerar um relatorio de uma reunião