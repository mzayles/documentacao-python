# DESAFIO 05

""" Crie um programa que dados o valor, da taxa e o tempo, efetuar o cálculo do valor de
uma prestação em atraso.
FÓRMULA: valor da prestação + (valor da prestação * (taxa / 100) * tempo) """

valor_prestacao = float(input("Digite o valor da prestação: R$ "))
taxa = float(input("Digite a taxa da prestação: "))
tempo = int(input("Digite o tempo da prestação (meses): "))

print(f"\nO valor da prestação em atraso é de R$ \033[1;31m{valor_prestacao + valor_prestacao * (taxa / 100) * tempo:,.2f}\033[0m.") # (;,.Xf)