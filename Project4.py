import random
# Rock

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_img = [Rock,Paper,Scissors]
user_choice = int(input(" Choose '0' for rock , '1' for paper and '2' for Scissors "))

if user_choice>0 and user_choice<3:
    print("You chose: ")
    print(game_img[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_img[computer_choice])

    if user_choice == 0:
        if computer_choice ==0:
            print("Game Draw! 😏")
        elif computer_choice == 1:
            print("You Lose! 🤐")
        else:
            print("You Win! 😎")

    if user_choice == 1:
        if computer_choice ==0:
            print("You Win! 😎")
        elif computer_choice == 1:
            print("Game Draw! 😏")
        else:
            print("You Lose! 🤐")

    if user_choice == 2:
        if computer_choice ==0:
            print("You Lose! 🤐")
        elif computer_choice == 1:
            print("You Win! 😎")
        else:
            print("Game Draw! 😏")

else:
    print("Invalid Choice!")
