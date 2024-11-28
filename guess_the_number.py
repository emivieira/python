# -*- coding: utf-8 -*-
import random

print('''===============================================
ADIVINHE O NÚMERO
===============================================

É hora de jogar! Tente adivinhar qual é o número secreto que selecionamos.\n''')

def new_game():
    return random.randint(1, 1000), 0

number, attempts = new_game()
playing = True

while playing:

  answer = input('Escolha um número entre 1 e 1000 (ou digite SAIR para encerrar a partida): ')

  try:

    if answer.upper() == "SAIR":
      print(f'\nJogo encerrado. O número era {number}.\nAté a próxima!')
      playing = False
    else:
      guess = int(answer)

      if guess < 1 or guess > 1000:
        print("Número fora do intervalo necessário.  Tente novamente.\n")
      else:
        attempts += 1

        #Verificar palpite
        if guess > number:
          print("\nO número é mais baixo do que este. Tente novamente.\n")
          attempts += 1
        elif guess < number:
          print("\nO número é mais alto do que este. Tente novamente.\n")
          attempts += 1
        else:
          print(f'\nParabéns, você acertou o número!\nVocê fez {attempts + 1} tentativa(s) para encontrar o número "{number}".')
          # Verificar se deve iniciar nova partida
          while True:
            restart = input("\nQuer jogar novamente? (S/N) ")
            if restart.upper() == "S":
              number, attempts = new_game()
              print(f'\nTemos um novo número! Tente adivinhar qual é.')
              break
            elif restart.upper() == "N":
              playing = False
              print(f'\nJogo encerrado.\nAté a próxima!')
              break
            else:
              print("\nEntrada inválida. Por favor, digite S para jogar novamente ou N para encerrar.\n")
  except ValueError:
      print("Entrada inválida. Por favor, insira um número ou digite SAIR para encerrar.\n")