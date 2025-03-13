# CORREÇÃO 5.1

valor = float(input("Digite o valor da prestação: R$ "))
taxa = float(input("Digite a taxa da prestação: "))
tempo = int(input("Digite a qtd de meses em atraso: "))
prestacao = valor + valor * (taxa / 100) * tempo

print(f"\nValor atualizado: R$ {prestacao:,.2f}") # formatando para casas decimais (:,.Xf)