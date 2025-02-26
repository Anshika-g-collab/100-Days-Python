'''
Your program should allow you to enter the position of the treasure using a two-digit system. 
The first digit is the horizontal coloumn number and the second digit in the vertical row number-
'''

row1 = ["👻","👻","👻"]
row2 = ["👻","👻","👻"]
row3 = ["👻","👻","👻"]
map = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
position = input("Where do you want to put the treasure?")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal -1]=" X "

print(f'{row1}\n{row2}\n{row3}')