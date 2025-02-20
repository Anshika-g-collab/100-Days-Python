num_char = len(input("Enter your name: "))
#print("Your name has" + num_char + "characters.") -- cannot concatenate string and int type (type error)
new_num_char = str(num_char)#TypeCasting
print("Your name has " + new_num_char + " characters.")
print(type(num_char))
print(70 + float("100.5"))
print(str(70)+str(100))