import random
print("Lets guess a number 1 - 20") 

computer_no=random.randint(1,20) #store the random numbers generated using random


guessesTaken = 0
score=5

while guessesTaken < 5:
    guess=int(input("What is your guess?")) #user input

    guessesTaken = guessesTaken + 1

    if guess == computer_no:
        score = 5-guessesTaken
        s=str(score)
        
        print('You win with a score of ' + s)

    elif guess > computer_no:
        print('Your guess is too high')

    else:
        print ('Your guess is too low.')

if guess == computer_no:
    
    print("Done")


else:
    print("You lose.The computer guessed number is  " + str(computer_no)) 
