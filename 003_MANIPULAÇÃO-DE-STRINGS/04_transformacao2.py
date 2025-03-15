# TRANSFORMAÇÃO DE STRINGS

# substituir palavras
print(frase.replace('SENAI', 'ESCOLA'))
print(frase)
frase = frase.replace('SENAI', 'ESCOLA')
print(frase)

frase2 = "   oi    SENAI   Ary Torres oi  "

# retirada/limpeza das extremidades
# não é definitivo, no próximo print aparece a frase original
print(frase2.strip())
print(frase2.strip())

# limpar espaços antes e depois
# os espaços do meio não são retirados
frase2 = frase2.strip()

print(frase2.strip('oi'))

url = 'https://google.com/h'
print(url.rstrip('h'))

print(url.lstrip('https://'))