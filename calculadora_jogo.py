import random
from colorama import Fore, init

init(autoreset=True)


# ---------------- FUNÇÕES ---------------- #

def menu():
    print()
    print(Fore.CYAN + 4 * '=*=')
    print(Fore.CYAN + '[1] somar')
    print(Fore.CYAN + '[2] diminuir')
    print(Fore.CYAN + '[3] multiplicar')
    print(Fore.CYAN + '[4] dividir')
    print(Fore.CYAN + '[5] inserir desconto')
    print(Fore.CYAN + '[6] Jogo de adivinhação')
    print(Fore.CYAN + '[7] sair')


def pedir_dois_numeros():
    try:
        a = float(input(Fore.CYAN + 'Digite um número: '))
        b = float(input(Fore.CYAN + 'Digite outro número: '))
        return a, b
    except ValueError:
        print(Fore.RED + '❌ Digite somente números!')
        return None, None


def somar():
    a, b = pedir_dois_numeros()
    if a is not None:
        print(Fore.GREEN + f'Soma = {a + b}')


def diminuir():
    a, b = pedir_dois_numeros()
    if a is not None:
        print(Fore.GREEN + f'Subtração = {a - b}')


def multiplicacao():
    a, b = pedir_dois_numeros()
    if a is not None:
        print(Fore.GREEN + f'Multiplicação = {a * b}')


def divisao():
    a, b = pedir_dois_numeros()
    if a is not None:
        if b == 0:
            print(Fore.RED + '❌ Não é possível dividir por zero.')
        else:
            print(Fore.GREEN + f'Divisão = {a / b}')


def desconto():
    try:
        d = float(input(Fore.CYAN + 'Digite o desconto entre 10 e 30: '))
        a = float(input(Fore.CYAN + 'Digite o valor do produto: '))

        if d < 10 or d > 30:
            print(Fore.RED + '❌ Desconto inválido.')
        else:
            preco_final = a - (a * d / 100)
            print(Fore.GREEN + f'Preço final = {preco_final:.2f}')
    except ValueError:
        print(Fore.RED + '❌ Digite somente números!')


def jogo():
    print()
    print(Fore.YELLOW + 'JOGO DA ADIVINHAÇÃO')
    print(Fore.YELLOW + 'Você terá 3 tentativas.')
    print()

    numero = random.randint(1, 10)

    for tentativa in range(1, 4):
        try:
            palpite = int(input(Fore.CYAN + 'Digite um número entre 1 e 10: '))

            if palpite == numero:
                print(Fore.GREEN + f'🎉 Você acertou na tentativa {tentativa}!')
                return
            elif palpite > numero:
                print('Chutou alto.')
            else:
                print('Chutou baixo.')

        except ValueError:
            print(Fore.RED + '❌ Digite somente números!')

    print(Fore.RED + f'❌ Você perdeu! O número era {numero}.')


# ---------------- CONTROLADOR ---------------- #

def main():
    while True:
        menu()

        try:
            opcao = int(input(Fore.CYAN + 'Escolha uma opção: '))
        except ValueError:
            print(Fore.RED + '❌ Digite somente números!')
            continue

        if opcao == 1:
            somar()
        elif opcao == 2:
            diminuir()
        elif opcao == 3:
            multiplicacao()
        elif opcao == 4:
            divisao()
        elif opcao == 5:
            desconto()
        elif opcao == 6:
            jogo()
        elif opcao == 7:
            print(Fore.YELLOW + 'Saindo... 👋')
            break
        else:
            print(Fore.RED + '❌ Opção inválida.')


# ---------------- INÍCIO DO PROGRAMA ---------------- #

main()
