

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques): 
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
   
    return saldo, extrato, numero_saques


def depositar(saldo, valor_deposito, extrato, /):    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [user for user in usuarios if user["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    usuario_existente = filtrar_usuario(cpf, usuarios)
    
    if usuario_existente:
        print("\n@@@ Já existe um usuário com este CPF! @@@")
        return

    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(novo_usuario)

    print("\n=== Usuário criado com sucesso! ===")

def  criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        nova_conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(nova_conta)
        print("\n=== Conta criada com sucesso! ===")
        return
        
    print("\n@@@ Usuário não encontrado! A criação da conta foi cancelada. @@@")

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
    print("\n" + "=" * 40)
    for conta in contas:
        print(f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)
    print("=" * 40)
    
    
def menu():
    menu_texto = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(menu_texto).lower()


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()