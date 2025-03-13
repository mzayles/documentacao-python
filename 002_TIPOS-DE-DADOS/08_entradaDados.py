# ENTRADA DE DADOS (INPUT)

numeroInteiro = int(input("Digite um número inteiro: "))
print(numeroInteiro)

numeroDecimal = float(input("\nDigite um número decimal: ")) # separador de decimal: . (não vírgula)
print(numeroDecimal)

valorLogico = bool(input("\nDigite algo: ")) # verificar se a pessoa digitou algo
print(valorLogico)

# não há necessidade declarar str() para o input()
texto = str(input("\nDigite um valor alfanumérico:\n"))
print(texto)