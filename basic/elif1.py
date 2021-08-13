import random

ans1="1. cat"
ans2="2. dog"
ans3="3. goat"
ans4="4. tortoise"
ans5="5. kitten"

print ("Select the pet")

print(ans1, ans2, ans3, ans4, ans5, sep="\n")
print()
ques=input("Which is the most suitable pet for keeping in a flat?\n")

choice=random.randint(1,5)
 

if choice==1:
    answer=ans1

elif choice==2:
    answer=ans2

elif choice==3:
    answer=ans3

elif choice==4:
    answer=ans4

else:
     answer=ans5

print()
print(choice)
print(answer)            
