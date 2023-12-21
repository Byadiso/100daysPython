# Day 7 
# Hangman project
import random 

words = ["titanic","kigali","Poland","eat"]

choicedWord = random.choice(words)


display= []
print(choicedWord)

for leter in choicedWord:
    display +="_"

print(display)
end_of_game = False

while not end_of_game:
    guess= input("Guess a letter to save your man:\n").lower()

    for position in range(len(choicedWord)):
        letter = choicedWord[position]
        if letter ==guess:
            display[position] = letter     

    print(display)

    if "_" not in display:
        end_of_game = True

