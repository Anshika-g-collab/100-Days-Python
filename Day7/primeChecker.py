num = int(input("Check this number: "))
def prime_checker(number):
    count = 0
    for i in range(2,number//2):
        if number>1:
            if number%i==0:
                count+=1
    if count==0:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a non-prime!")
prime_checker(number = num)