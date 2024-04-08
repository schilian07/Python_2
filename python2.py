print("Programa Expresso")

print("1- Cadastrar Restaurante")
print("2- Listar Restaurante")
print("3- Ativar Restaurante")
print("4- Sair")

opcao_digitada = int(input("Selecione uma opção: "))

if (opcao_digitada == 1):
    print("Você escolheu a opção cadastrar restaurante")
elif(opcao_digitada == 2):
    print("Você escolheu a opção Listar restaurante")
elif(opcao_digitada == 3):
    print("Você escolheu a opção Ativar restaurante")
elif(opcao_digitada == 4):
    print("Você escolheu Sair")            

else:
    print("Opção invalida tente novamente")