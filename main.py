from art import logo, stages
from allwords import word_list
import random
lives=6
chosenWord= random.choice(word_list)
print(logo)

  #Generar la lista en blanco
print(chosenWord)
list=[]
for i in range(len(chosenWord)):
    list += "_"

end_of_game=False
while not end_of_game:
    userGuess=input('Guess a letter: ').lower()
    if userGuess in list:
      print(f'Ya has intentado la letra:{userGuess}')
    for x in range(len(chosenWord)):
          letter = chosenWord[x]
          if letter == userGuess:
              list[x]= letter
    print(list)

    if "_" not in list:
      end_of_game=True
      print('You Win!')
    if userGuess not in chosenWord:
      lives-=1
      print(f'The letter: {userGuess}, is not in the word')
      print(stages[lives]) #lives aplica como index porque son Int.
    if lives==0:
      end_of_game=True
      print('You lose!')