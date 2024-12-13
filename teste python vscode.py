deposito_inicial = float(input("Digite o valor do depósito inicial: R$ "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal (%): "))

# Converte a taxa de juros de percentual para decimal
taxa_juros_mensal /= 100

# Inicializa variáveis
saldo = deposito_inicial
total_juros = 0

print("\nMês | Saldo no início do mês | Juros ganhos | Saldo no final do mês")
print("---------------------------------------------------------------")

# Loop para calcular o saldo mês a mês por 24 meses
for mes in range(1, 25):
    juros_mensal = saldo * taxa_juros_mensal  # Calcula o juros do mês
    saldo += juros_mensal  # Atualiza o saldo com os juros
    total_juros += juros_mensal  # Acumula os juros ganhos
    
    # Exibe o saldo no início do mês, o valor dos juros e o saldo final
    print(f"{mes:3} | R$ {saldo - juros_mensal:,.2f}           | R$ {juros_mensal:,.2f}   | R$ {saldo:,.2f}")

# Exibe o total ganho com juros ao final do período
print(f"\nTotal ganho com juros após 24 meses: R$ {total_juros:,.2f}")