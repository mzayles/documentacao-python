# CORREÇÃO 11.1

print('\033[1;33;42m'," CARDÁPIO ".center(40, '#'),'\033[0m\n')

print(f"{'Pastel'.ljust(32, '.')}"f"{'R$ 6,50'.rjust(10, '.')}") # '': o programa entende que é uma string normal, caso contrário, as "" encerraria f string.
print(f"{'Coxinha'.ljust(32, '.')}"f"{'R$ 16,50'.rjust(10, '.')}")
print(f"{'Risoles de queijo'.ljust(32, '.')}"f"{'R$ 156,50'.rjust(10, '.')}")