#início das Variáveis Globais
lista_colaboradores = []
id_global = 0
#fim das Variáveis Globais

#início de cadastrar_colaboradores()
def cadastrar_colaboradores(id):
  print('Bem-vindo ao menu de Cadastrar Colaborador')
  print('ID do colaborador: {}'.format(id))
  nome = input('Digite o nome do colaborador: ')
  setor = input('Digite o setor do colaborador: ')
  pagamento = float(input('Digite o salário(R$) do colaborador: '))
  dicionario_colaboradores = {'id'      : id,
                        'nome'          : nome,
                        'setor'         : setor,
                        'pagamento'     : pagamento}
  lista_colaboradores.append(dicionario_colaboradores.copy())
#fim de cadastrar_colaboradores()

#início de consultar_colaborador()
def consultar_colaborador():
  print('Bem-vindo ao menu Consultar Colaborador')
  while True:
    opcao_consultar = input('\nEscolha a opção desejada:\n'+
                          '1- Consultar todos os colaboradores\n'+
                          '2- Consultar colaborador por id\n'+
                          '3- Consultar por setor\n'+
                          '4- Retornar ao menu\n'+
                          '>>')
    if opcao_consultar == '1':
      print('Você escolheu a opção consultar todos os colaboradores')
      for colaboradores in lista_colaboradores: #vai varrer toda a lista de colaborador
       print('--------------------')
       for key, value in colaboradores.items(): #varrer todos os itens
          print('{} : {}'.format(key,value))
       print('--------------------')
    elif opcao_consultar == '2':
      print('Você escolheu a opção consultar produto por id')
      id_desejado = int(input('Digite o id desejado: '))
      for colaboradores in lista_colaboradores:
        if colaboradores['id'] == id_desejado: #o id do campo é igual o valor desejado
          print('--------------------')
          for key, value in colaboradores.items(): #varrer todos os itens
            print('{} : {}'.format(key,value))
        print('--------------------')
    elif opcao_consultar == '3':
      print('Você escolheu a opção consultar por setor')
      id_desejado = input('Digite o setor desejado: ')
      for colaboradores in lista_colaboradores:
        if colaboradores['setor'] == id_desejado: #o id do campo é igual o valor desejado
          print('--------------------')
          for key, value in colaboradores.items(): #varrer todos os itens
            print('{} : {}'.format(key,value))
        print('--------------------')
    elif opcao_consultar == '4':
      return #sai da função e volta para o Main
    else:
      print('Opção Inválida. Tente Novamente!')
      continue #volta para o início
#fim de consultar_colaboradores()

#início de remover_colaborador()
def remover_colaborador():
  print('Bem-vindo ao menu de Remover Colaborador')
  id_desejado = int(input('Digite o id do colaborador que deseja remover: '))
  for colaboradores in lista_colaboradores:
    if colaboradores ['id'] == id_desejado:
      lista_colaboradores.remove(colaboradores)
      print('Colaborador Removido!')
#fim de remover_colaborares()

#Início do Main
print('Bem-vindo ao Controle de Colaboradores da Lorena Muller')
while True:
  opcao_principal = input('\nEscolha a opção desejada:\n'+
                          '1- Cadastrar Colaborador\n'+
                          '2- Consultar Colaborador\n'+
                          '3- Remover Colaborador\n'+
                          '4- Encerrar Programa\n'+
                          '>>')
  if opcao_principal == '1':
    cadastrar_colaboradores(id_global)
    id_global += 1
  elif opcao_principal == '2':
    consultar_colaborador()
  elif opcao_principal == '3':
    remover_colaborador()
  elif opcao_principal == '4':
    break #encerra o laço e fim do programa
  else:
    print('Opção Inválida. Tente Novamente!')
    continue #volta para o início
