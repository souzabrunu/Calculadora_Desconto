print("------------------------------------")
print("   Calculadora de Descontos Pro   ")
print("------------------------------------")
print("Bem-vindo! Este programa calcula o valor final de um produto.")
print("Você precisará informar o valor original e a porcentagem de desconto.\n")

while True:
    try:
        n = float(input('Digite o valor original do produto: '))
        p = float(input('Digite a porcentagem de desconto ex: 15 para 15%: '))

        if n < 0 or p < 0:
            print("\nERRO: Por favor, digite apenas valores positivos.\n")
            continue
        
        break

    except ValueError:
        print("\nERRO: Você digitou algo que não é um número.")
        print("Por favor, tente novamente.\n")

d = n * (p / 100)
valor_final = n - d

print("\n--- Resumo do Cálculo ---")
print(f'Valor original:      R$ {n:.2f}')
print(f'Desconto ({p}%):    - R$ {d:.2f}')
print(f'Valor final a pagar: R$ {valor_final:.2f}')