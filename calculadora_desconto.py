from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "------------------------------------")
print(Fore.CYAN + "   Calculadora de Descontos Pro   ")
print(Fore.CYAN + "------------------------------------")
print("Bem-vindo! Este programa calcula o valor final de um produto.")
print("Você precisará informar o valor original e a porcentagem de desconto.\n")

while True:
    try:
        n = float(input('Digite o valor original do produto: '))
        p = float(input('Digite a porcentagem de desconto (ex: 15 para 15%): '))

        if n < 0 or p < 0 or p > 100:
            print(Fore.RED + "\nERRO: Por favor, digite valores positivos e desconto entre 0% e 100%.\n")
            continue
        
        break

    except ValueError:
        print(Fore.RED + "\nERRO: Você digitou algo que não é um número.")
        print("Por favor, tente novamente.\n")

d = n * (p / 100)
valor_final = n - d

print("\n--- Resumo do Cálculo ---")
print(f'Valor original:       R$ {n:,.2f}')
print(f'Desconto ({p:.0f}%):  {Fore.YELLOW}- R$ {d:,.2f}')
print(f'Valor final a pagar:  {Fore.GREEN}R$ {valor_final:,.2f}')
