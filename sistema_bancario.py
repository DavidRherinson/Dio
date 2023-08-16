menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = float(500)
extrato = {
     "Extrato Geral": []
}
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "d":
       deposito = float(input("Digite o valor do deposito: R$"))
       if deposito > 0:
           saldo += deposito
           extrato["Extrato Geral"].append(f"valor depositado: R${deposito:.2f}")
       else:
          print("Digite um valor acima de 0")
    
    elif opcao == "s":
        if numero_saques <= limite_saque:
            valor_saque = float(input("Valor de saque: R$ "))

            if valor_saque > 0:
                if valor_saque <= limite and valor_saque <= saldo:
                    extrato["Extrato Geral"].append(f"Saque Realizado no valor de: R${valor_saque:.2f}")
                    print("Saque Realizado com Sucesso!")
                    numero_saques += 1
                    saldo = saldo - valor_saque   
                elif valor_saque > saldo:
                    print("Saldo insuficiente")     
                else:
                    print(f"O limite de saque é de {limite:.2f}")    
            else:
              print("Informe um valor valido")
        else:
            print("Você exedeu o limite de saque diario")

    elif opcao == "e":
        for extrato_geral in extrato["Extrato Geral"]:
            print(extrato_geral)

    elif opcao == "q":
        break

    else:
        print("operação inválida, por favor selecione novamento a operação desejada.") 

print("Volte sempre nosso Banco agradece")