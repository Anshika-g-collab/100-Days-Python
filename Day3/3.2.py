print("Welcome to Rollercoaster!!!")
height = int(input("What is your height in cm? "))

if height>120:
    age = int(input("What is your age?"))
    if age <=18:
        print("Please pay : Rs 700")
    else:
        print("Please pay : Rs 1000")
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")