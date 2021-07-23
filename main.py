import random

palpite, tentativas = "", 0

frutas = ['maçã', 'laranja', 'pera', 'Melancia', 'uva', 'morango']
fruta_preferida = random.choices(frutas)[0].upper()
while palpite != fruta_preferida:
  print(frutas)
  palpite = input('qual a fruta preferida?\n> ')
  palpite = palpite.upper()
  
  tentativas += 1
  if palpite != fruta_preferida:
    print("Você errou não é essa fruta")
else:
  print(f"Parabéns você acertou após {tentativas} tentativas")
  
