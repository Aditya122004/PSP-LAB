import random
num=random.randint(1,50)
print("You have 5 guesses")
win=False
turn=1
while(turn<6):
    n=int(input("Enter your guess: "))
    if(n==num):
        print("Congratulations You have won the game")
        win=True
        break
    elif(n>num):
        print("Guess a lower number")
        
    else:
        print("Guess a higher number")
    if(turn!=5):
        print(f"You have {5-turn} guesses left")
    turn=turn+1
if(win==False):
    print("The number was",num)
