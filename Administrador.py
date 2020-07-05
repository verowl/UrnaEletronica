import getpass
import sys
def cadastraSenhaSecretario():
    print("Cadastre a senha do Secretario")
    SenhaSecretario = getpass.getpass(stream=sys.stderr)
    set_senhaSecretario.Secretario(SenhaSecretario)


