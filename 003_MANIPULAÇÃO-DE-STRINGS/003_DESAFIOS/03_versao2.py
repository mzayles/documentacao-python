# CORREÇÃO 03.1

frase = input("Digite uma frase: ").lower()

print(f"\nA frase tem {frase.count('a')} letras A!")
print(f"Letra A 1ª vez na {frase.find('a')+1}ª posição!")
print(f"Letra A última vez na {frase.replace(' ', '').rfind('a')+1}ª posição!")