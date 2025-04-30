import random
import time
p1=input("Enter the 1st player name: ")
p2=input("Enter the 2nd player name: ")
a=int(input("Enter the minimum number of the range: "))
b=int(input("Enter the maximum number of the range: "))
# guessing game main code
def guessing():
    correct=0
    guesscount=1
    specialnumber=random.randint(a,b) #genrating a random number from the taken range
    while(correct==0):
        guess=int(input("Enter a number: "))
        if guess<specialnumber:
            print("A little higher, Try again")
            guesscount=guesscount+1
        elif guess>specialnumber:
            print("A little lower, Try again")
            guesscount=guesscount+1
        else:
            print("You guessed correctly")
            print("You completed in",guesscount,"Turns")
            correct=1
            return guesscount
print("Playe 1 turn:")
pt1=guessing()
print("Player 2 turn")
pt2=guessing()
# Logic for determining who won
if pt1<pt2:
    print(f'{p1} won')
elif pt1==pt2:
    print("Tie")
else:
    print(f'{p2} won')
time.sleep(7)