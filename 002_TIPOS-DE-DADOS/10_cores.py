# CORES

"""
\033[ESTILO;FONTE;FUNDOm TEXTO \033[0m
\033[m    \033[0m

|033[m: colocar cor
\033[0m: break

Estilos: 0 nenhum | 1 negrito | 3 itálico | 4 sublinhado
"""

print("\033[3;36m HELLO, WORLD")
print("\033[0;32m HELLO, MARIANA\n")

print("\033[1;33;45m   TEXTO   \033[0m")

# cores de fonte
print("\033[30m CINZA")
print("\033[31m VERMELHO")
print("\033[32m VERDE")
print("\033[33m AMARELO")
print("\033[34m CIAN")
print("\033[35m MAGENTA")
print("\033[36m AZUL")
print("\033[37m BRANCO")

# cores de fundo
print("\033[40m CINZA")
print("\033[41m VERMELHO")
print("\033[42m VERDE")
print("\033[43m AMARELO")
print("\033[44m CIAN")
print("\033[45m MAGENTA")
print("\033[46m AZUL")
print("\033[47m BRANCO")

print("\033[1;33;45m\033[2m\033[3m\033[4m   TEXTO   \033[0m")