import random 
import hangman_visuals
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False

lives = 0

print("🎮 Welcome to Hangman! 🎮")
print(hangman_visuals.logo)
display = []
for letter in chosen_word:
     display+="_"
print(f"The word has following blank spaces : \n")
print(f"{' '.join(display)}")
print(hangman_visuals.stages[lives])
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

    print(hangman_visuals.stages[lives])

         
    
