# EXEMPLO ANÁLISE DE STRINGS

num = input("Digite um número ")
if num.isnumeric():
    num = int(num)
else:
    print("Não é número!")

print(type(num))