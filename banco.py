menu = '''
 Banco Antonio Victor

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''
    
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_DE_SAQUES = 3

# corrigir opcao para string e depois inteiro...
while True:

    opcao = input(menu)
    try:
        opcao_int = int(opcao)
        if opcao_int == 1:
            print('- Depósito: ') 
            deposito = input('Valor do depósito: ')

            try:
                deposito_int = int(deposito)
            
                if deposito_int <=0:
                    print('Depósito precisar ser maior que (0) zero.\nTente novamente.')
                else:    
                    print(f"""
 --- Déposito ---
Saldo anterior R${saldo:.2f}
Valor do depósito R${deposito_int:.2f}
Saldo atual R${deposito_int+saldo:.2f}
""")
                    saldo += deposito_int
                    extrato += f'Depósito de R${deposito_int:.2f}, Saldo R${saldo:.2f}.\n'
                
                
            except ValueError:
                print("Só são permitidos números para essa operação.\nTente novamente.")
            
    
        if opcao_int == 2:
            print('- Saque:')
            saque  = input('Valor do saque: ')
            try:
                saque_int = int(saque)
            
                if saque_int <=0:
                    print('Saque precisar ser maior que (0) zero.\nTente novamente.')
                else:    
                    if LIMITE_DE_SAQUES == numero_saques:
                        print("Limite Diário acabou!\nTente outro dia")
                    elif saque_int > saldo:
                        print(f"Não há saldo suficiente, seu saldo atual é de RS:{saldo:.2f}")
                    elif saque_int > 500:
                        print(f"Limite de saque é de R${limite:.2f} por operação")
                    else:
                        numero_saques += 1
                        print(f"""
--- Sacando ---
Saldo atual R${saldo:.2f}
Valor do Saque R${saque_int:.2f}
Saldo restante R${saldo-saque_int:.2f}
                          """)
                        saldo -= saque_int
                        extrato += f'Saque de R${saque_int:.2f}, Saldo R${saldo:.2f}.\n'

            except ValueError:
                print("Só são permitidos números para essa operação.\nTente novamente.")


        if opcao_int == 3:
            print('- Extrato: ') 
            print(extrato)
        if opcao_int == 0:
            print('Saindo...\nVolte sempre!')
            break
    except ValueError:
        print("Só são permitidos números para essa operação.\nTente novamente.")
