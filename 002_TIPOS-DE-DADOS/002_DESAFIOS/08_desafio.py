# DESAFIO 08

""" Solicite ao usuário o valor do salário atual, em seguida solicite o
percentual de aumento e imprima o valor do salário atualizado. """

salario_atual = float(input("Digite o seu salário atual: R$ "))
percentual_aumento = float(input("Digite o percentual de aumento: "))
salario_final = salario_atual + (salario_atual * (percentual_aumento / 100))

print(f"\n\033[4mSalário atualizado:\033[0m R$ {salario_final:,.2f}.")