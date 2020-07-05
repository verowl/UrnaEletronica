var



print "A Urna foi inicializada. Caro Administrador, informe sua senha e cadastre o secretário)"
cadastraSenhaSecretario.Administrador()
print "Caro Secretário - TSE cadastre os usuários e senhas dos participantes da zona"
cadastraSenhas.Secretario()


cadastraPresidente.Secretario(senhaSecretario)
cadastraMesario.Secretario(senhaSecretario)
cadastraCandidatos.Secretario(senhaSecretario)
cadastraEleitor.Secretario(senhaSecretario)
print "Presidente, digite sua senha para abrir os trabalhos da Urna"
abreUrna.Presidente()
print "Mesário, digite sua senha para abrir a votação"
abreVotacao.Mesario()
print "Esta é uma urna eletrônica"
vota.Eleitor()
confirmaVoto.Mesario()
print "Voto computado"
print "Selecione uma opção"
    Abrir nova votação
    Finalizar votação
    Alterar para usuário Administrador
print "Caro Presidente. Digite sua senha para a totalização dos votos e encerramento da Urna"
encerraVotacao.Presidente()
