'''
You are painting a wall. the instructions on the paint says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall 
'''

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height = test_h , width=test_w ,cover = coverage):
    number_of_cans = (height*width)/cover
    return round(number_of_cans)
print(f"Required number of cans are: {paint_calc()}")