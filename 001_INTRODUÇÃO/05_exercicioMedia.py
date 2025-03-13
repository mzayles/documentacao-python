# EXEMPLO DIAGRAMA: EXERCÍCIO DE MÉDIA

nota1 = 0
nota2 = 0
media = 0

nota1 = float(input("Digite a 1ª nota: ")) # operador FLOAT()
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2 # aritmética

if media >= 5:
    print('Aprovado')
else:
    print('Reprovado')