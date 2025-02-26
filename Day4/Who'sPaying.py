import random
Members = input("Enter everybody's name, separated by comma: ")
Member_list = Members.split(',')
payer = (Member_list[random.randint(0,len(Member_list))])

print("The bill is on 'payer'!!!")