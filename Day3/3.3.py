print("Welcome to the rollercoaster !")
height = int(input("What is your height?"))

if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 500
        print("Child tickets are Rs. 500.")
    elif age <=18:
        bill = 700
        print("Youth tickets are Rs. 700.")
    else:
        bill = 1000
        print("Adult tickets are Rs. 1000.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == 'Y':
        bill=bill+100
    print(f"Your final bill is {bill}")


else:
    print("Sorry, you have to grow taller before you can ride.")