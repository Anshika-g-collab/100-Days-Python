import random 

word_list = ["camel","killer","awkward","galaxy","rhythm",'force',"tug","borrow","antibacterial","cake"]

# Randomly choose a word from the word_list and assign it to a variable called choosen_word.

choosen_word = random.choice(word_list)

# Create an empty list called 'Display' .
# for each letter in the choosen_word , add a "_" to 'display'.

display = []
for letter in choosen_word:
     display.append("_")
print(display)

# ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("\nGuess a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# print(choosen_word).

for n in range(0,len(choosen_word)):
    if choosen_word[n] == guess:
         display[n] = guess

print(display)
         
    
