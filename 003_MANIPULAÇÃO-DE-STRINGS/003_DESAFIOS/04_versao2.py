# CORREÇÃO 04.1

nome_completo = input("Digite seu nome completo: ")

print(f"\nPrimeiro nome: {nome_completo.title().split()[0]}")
print(f"Último nome: {nome_completo.title().split()[-1]}")