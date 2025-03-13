# DESAFIO 06

""" Dado a nota das provas P1, P2 e P3, calcular a média (aritmética) das notas do aluno. """

prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))

print(f"\nA sua média é de \033[1;32m{(prova1 + prova2 + prova3) / 3:,.1f}\033[0m.")