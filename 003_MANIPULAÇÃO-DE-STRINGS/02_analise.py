# ANÁLISE DE STRINGS

frase = "SENAI Ary Torres"

# tamanho da string
print(len(frase))

# contar caracteres
print(frase.count('r'))

# encontrar índice (retorna -1 se não encontrar)
print(frase.find('z'))

# encontrar índice (a partir da direita)
# índice que vem primeiro na direita
print(frase.rfind('r'))

# encontrar índice (gera erro se não encontrar)
print(frase.index('r'))

# vericar pertinência
# a palavra 'Ary' está na variável frase?
print('Ary' in frase)