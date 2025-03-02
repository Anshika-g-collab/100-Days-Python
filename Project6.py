import random 

word_list = ["camel","killer","awkward","galaxy","rhythm",'force',"tug","borrow","antibacterial","cake"]

#TODO_1 - Randomly choose a word from the word_list and assign it to a variable called choosen_word.

choosen_word = random.choice(word_list)

for letter in choosen_word:
     print("_",end=" ")

#TODO_2 - ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("\nGuess a letter: ").lower()

#TODO_3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in choosen_word:
    if letter == guess:
         print("Right")
    else:
         print("Wrong")
