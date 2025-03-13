# CORREÇÃO 02.1

caractere1 = input("Digite o primeiro caractere: ")
caractere2 = input("Digite o segundo caractere: ")

print(f"\nO usuário digitou \033[1;32m{caractere1}\033[0m " # técnica quebra de linha
      f"e \033[1;36m{caractere2}\033[0m!")