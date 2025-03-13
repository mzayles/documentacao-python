# REFATORAÇÃO: melhorar o código sem alterar seu comportamento externo.

# ORIGINAL
a = 10
b = 20
c = a + b

print('Original', c)

# REFATORADO
def soma(x, y): # FUNÇÃO DEF(argumento1, argumento2)
    return x + y

print('Refatorado', soma(45, 48))