#Dice Rolling Simulator
import random

def rollthedice(dice_number):
  print(f"\nQUE ROLEM OS DADOS!")
  for i in range(dice_number):
    face = random.randint(1, 6)
    showface(face)

def showface(face):
  faces = { 1: '''
     _____________
    |             |
    |             |
    |      O      |
    |             |
    |_____________|
  ''', 2: '''
     _____________
    |             |
    |        O    |
    |             |
    |   O         |
    |_____________|
  ''', 3: '''
     _____________
    |             |
    |         O   |
    |      O      |
    |   O         |
    |_____________|
  ''', 4: '''
     _____________
    |             |
    |   O     O   |
    |             |
    |   O     O   |
    |_____________|
  ''', 5: '''
     _____________
    |             |
    |   O     O   |
    |      O      |
    |   O     O   |
    |_____________|
  ''', 6: '''
     _____________
    |             |
    |   O     O   |
    |   O     O   |
    |   O     O   |
    |_____________|
  '''
  }

  print(faces[face])

rolling = True

while rolling:
  dice_number = input("\nQuantos dados você quer jogar?\nEscolha um número de 1 a 5 (ou digite SAIR para encerrar): ")

  try:

    if dice_number.upper() == "SAIR":
      print("\nJogo encerrado. Até a próxima!")
      rolling = False
    else:
      dice_number = int(dice_number)
      if dice_number > 0 and dice_number < 6:

        #roll the dice
        rollthedice(dice_number)

        #restart
        while True:
          restart = input("\nQuer jogar novamente? (S/N) ")
          if restart.upper() != "S" and restart.upper() != "N":
            print("\nValor inválido.")
          elif restart.upper() == "N":
            print("\nJogo encerrado. Até a próxima!")
            rolling = False
            break
          else:
            break

      else:
        print("\nValor inválido. Escolha um número de 1 a 5.")
  except ValueError:
    print("\nValor inválido. Escolha um número de 1 a 5.")