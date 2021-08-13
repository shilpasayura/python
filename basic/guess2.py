import random

#store the random numbers generated using random
computer_no=random.randint(1,20) 

def sameno(target,number):
    if target == number:
        result = "Win"

    elif target>number:
         #computer number>my guess
         result = "Low"

    else:
        result="High"

    return result

print("Lets guess a number")      

guess=int(input("What is your guess?")) #user input

high_or_low=sameno(computer_no,guess)

while high_or_low != "Win":
    if high_or_low == "Low":
        guess=int(input("Too low. Try again"))

    else:
         guess=int(input("Too high. Try again"))   

    high_or_low=sameno(computer_no,guess)

input("Exit")
