import random

#store the random numbers generated using random
computer_no=random.randint(1,4) 

def sameno(target,number):
    if target == number:
        result = "Win"
    else:
        result="Fail"

    return result

print("Lets guess a number")      

guess=int(input("What is your guess?"))

print(sameno(computer_no,guess))  
