# DESAFIO 04

""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o ultimo nome separadamente.

Exemplo: Leandro Gomes Andrade

Primeiro: Leandro
Ultimo: Andrade """

nome_completo = input("Digite seu nome completo: ").split()

print(f"\033[1;32m\nPrimeiro\033[0m: {nome_completo[0].title()}")
print(f"\033[1;32mSegundo\033[0m: {nome_completo[1].title()}")