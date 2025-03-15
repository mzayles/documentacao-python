# CORREÇÃO 04.2 > EXEMPLO ÚLTIMO NOME

nome_completo = input("Digite seu nome completo: ")
print(f"Último nome: {nome_completo[nome_completo.rfind(' ')+1:]}")