import random 
# Raw strings (r"") tell Python to ignore escape sequences.
stages = [r'''
    +---+
    |   |
        |
        |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
        |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========
''',
r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========
''']
word_list = ["camel","killer","awkward","galaxy","rhythm",'force',"tug","borrow","antibacterial","cake"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

lives = 0

print("🎮 Welcome to Hangman! 🎮")
display = []
for letter in chosen_word:
     display+="_"
print(f"{' '.join(display)}")
print(stages[lives])
while not end_of_game :
    
    guess = input("\nGuess a letter: ").lower()

    for n in range(word_length):
        if chosen_word[n] == guess:
            display[n] = guess
            print(f" You guessed it right 👏")
    if guess not in chosen_word:
        lives+=1
        print(f"❌ Incorrect guess! You have {6-lives} lives left.")
        if lives == 6:
            end_of_game = True
            print(f"💀 Game Over! The word was: {chosen_word}")
    print(f"{' '.join(display)}")
    
    if '_' not in display:
        end_of_game = True
        print("🎉 Congratulations! You guessed the word! 🎉")

    print(stages[lives])

         
    
