'''
->if the bill of rupees 1500, split between 3 people , with 12% tip.
->each person should pay (1500/3)*1.12
->round up to two decimal places for precision
'''
print("Welcome to 'Tip Calculator'...")
bill = int(input("What was the total bill? "))
tip = int(input("What percentage tip you would like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill?"))
result = ((bill * (tip/100))+bill)/people
print(f"Each person should pay: Rs",result)
