def menu(func):
    print('1. Adicionar funcionario')
    print('2. Exibir todos os funcionarios')
    print('3. listar gerentes')
    print('4. listar chefes')
    escolha = int(input('Escolha uma opção: '))
    return escolha

def adicionar_funcionario():
    sair = 's'
    while sair != 'n':
        func = {}
        nome = input('Nome do funcionario: ').strip()

        func[nome] = input('Cargo do funcionario: ')
        funcionarios.append(func)
        sair = input('Deseja adicionar outro funcionario? [s/n] ').lower()
    print()

def exibir_funcionarios():
    if not funcionarios:
        print('Nenhum funcionário adicionado!')
    else:
        print('Funcionarios cadastrados:')
        print()
        for funcionario in funcionarios:
            for k, v in funcionario.items():
                print(f"{'Nome'}: {k} - {'Cargo'}: {v}")
    print()
        
def listar_gerente():
    if not funcionarios:
        print('Nenhum funcionário adicionado!')
    else:
        print('Gerentes cadastrados: ')
        print()
        verificação = False
        for funcionario in funcionarios:
            for k, v in funcionario.items():
                if v.lower() == 'gerente':
                    print(f'Nome: {k} - Cargo: {v}')
                    verificação = True
        if verificação == False:
            print('Nenhum gerente cadastrado!')

    print()

def listar_chefe():
    if not funcionarios:
        print('Nenhum funcionário adicionado!')
    else:
        print('Chefes cadastrados:')
        print()
        for funcionario in funcionarios:
            for k, v in funcionario.items():
                if v.lower() == 'chefe':
                    print(f'Nome: {k} - Cargo: {v}')
                else:
                    print('Nenhum chefe cadastrado!')
    print()
funcionarios = []

while True:
    escolha = menu(funcionarios)
    if escolha == 1:
        adicionar_funcionario()
    elif escolha == 2:
        exibir_funcionarios()
    elif escolha == 3:
        listar_gerente()
    elif escolha == 4:
        listar_chefe()

