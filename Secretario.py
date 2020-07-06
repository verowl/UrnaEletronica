import getpass
import sys
senhaSecretario = ""
candidatos=[]
def set_senhaSecretario(novaSenha):
    senhaSecretario= novaSenha
def cadastraSenhaMesario():
    print("Cadastre a senha do Mesario")
    SenhaMesario = getpass.getpass(stream=sys.stderr)
    set_senhaSecretario.Mesario(SenhaMesario)

def cadastraCandidatos():
        print("Cadastre os candidatos")
        while True:
                cod_candidato = int(input("Digite o numero do candidato"))
                nome_candidato= str(input("Digite o nome do Candidato"))
                part_candidato= str(input("Informe o partido do candidato"))
                candidatos.append([cod_candidato, nome_candidato, part_candidato])
                resposta = int(input("""Deseja cadastrar um novo candidato?
1.Sim
2.Nao
"""))
                if (resposta==2):
                       break

def cadastraEleitores():
        print("Cadastre os Eleitores")
        while True:
                nome_eleitor= str(input("Digite o nome do Eleitor"))
                senha_eleitor= getpass.getpass(stream=sys.stderr)
                eleitores.append([nome_eleitor,senha_eleitor])
                resposta = int(input("""Deseja cadastrar um novo Eleitor?
1.Sim
2.Nao
"""))
                if (resposta==2):
                       break
cadastraCandidatos()


