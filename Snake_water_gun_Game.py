'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youStr = input("Enter your choice : ")
youDict = {"s" : 1, "w": -1, "g": 0}
you = youDict[youStr]
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}

print(f"You Choose {reverseDict[you]}\n Computer Choose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw")

else:
    if(computer == -1 and you == 1):                 
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    else:
        print("something wrong")


