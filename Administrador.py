import getpass
import sys
def cadastraSenhaSecretario():
    print("Cadastre a senha do Secretario")
    SenhaSecretario = getpass.getpass(stream=sys.stderr)
    set_senhaSecretario.Secretario(SenhaSecretario)
def alteraSenhaSecretario():
    print("Altere a senha do Secretario")
    SenhaSecretario = getpass.getpass(stream=sys.stderr)
    set_senhaSecretario.Secretario(SenhaSecretario)
def alteraSenhaPresidente():
    print("Altere a senha do Presidente")
    SenhaPresidente = getpass.getpass(stream=sys.stderr)
    set_senhaPresidente.Secretario(SenhaPresidente)
def alteraSenhaMesario():
    print("Altere a senha do Mesario")
    SenhaMesario = getpass.getpass(stream=sys.stderr)
    set_senhaMesario.Secretario(SenhaMesario)
