def depositar(saldo, valor, extrato, /):
   
    if valor <=0:
            print('Depósito precisar ser maior que (0) zero.\nTente novamente.')
    else:    
        print(f"""

================ DEPÓSITO ================
Saldo Anterior:\t\tR${saldo:.2f}
Depósito de:\t\tR${valor:.2f}
Saldo Atual:\t\tR${valor+saldo:.2f}

==========================================
""")
        saldo += valor
        extrato += f'Depósito de R${valor:.2f}, Saldo R${saldo:.2f}.\n'
        return saldo, extrato
                
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        print(f"""

================ SAQUE ================
Saldo Anterior:\t\tR${saldo:.2f}
SAQUE de:\t\tR${valor:.2f}
Saldo Atual:\t\tR${saldo-valor:.2f}


---Máximo de Saque Por dia são 3---
Saque Feito Hoje: {numero_saques+1}
==========================================
""")
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato , numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas, linha):
    for conta in contas:
        linha += f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
       
    return linha


def main():


    menu = '''

================ BANCO AVPS ================
    [1] Criar Usuário
    [2] Criar Conta
    [3] Listar Conta 
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [0] Sair

==========================================
==> '''

    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    linha = ""
    usuarios = []
    contas = []    


    while True:

        opcao = input(menu)


        try:
            opcao_int = int(opcao)

            if opcao_int == 4:
                print('- Depósito: ') 
                valor_str = input('Valor do depósito: ')

                try:
                    valor = float(valor_str)
                    saldo, extrato = depositar(saldo, valor, extrato)
                
                
                except ValueError:
                    print("Só são permitidos números para essa operação.\nTente novamente.")
            
    
            if opcao_int == 5:
                print('- Saque:')
                valor_str  = input('Valor do saque: ')
                try:
                    valor = int(valor_str)

                    saldo, extrato, numero_saques = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_DE_SAQUES,
            )
                except ValueError:
                    print("Só são permitidos números para essa operação.\nTente novamente.")


            if opcao_int == 6:
               exibir_extrato(saldo, extrato=extrato)
            
            elif opcao == "1":
                criar_usuario(usuarios)

            elif opcao == "2":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            elif opcao == "3":
                listar_contas(contas, linha)
            elif opcao_int == 0:
                print('\nSaindo...\nVolte sempre!')
                break
        except ValueError:
            print("Só são permitidos números para essa operação.\nTente novamente.")
main()



