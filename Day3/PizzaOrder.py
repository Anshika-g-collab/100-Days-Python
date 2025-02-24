print("Welcome to Python 'Pizza Delivers!!' ")
size = input("What size pizza do you want? S,M or L? ")
add_pepperoni = input("Do you want 'Pepperoni'? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
     bill+=400
elif size == "M":
     bill+=500
elif size == "L":
     bill +=700

if add_pepperoni == "Y":
    if size == "S":
         bill+=50
    else:
         bill+=100
    
if extra_cheese == 'Y':
     bill+=100
print(f"Your final bill is :Rs{bill}")

