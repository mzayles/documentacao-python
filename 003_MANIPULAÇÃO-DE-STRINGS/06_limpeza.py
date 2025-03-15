# limpeza de string

novoTexto = "oi    SENAI   Ary   Torres   oi"

# limpeza das extremidades e transformação do texto em lista
novoTexto = novoTexto.strip('oi').split()
print(type(novoTexto))
print(' '.join(novoTexto))