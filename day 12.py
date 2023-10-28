#day 12


# builiding a guessing game
import random

hard_attemp = 5 
easy_attemp = 10
myNumber = random.randint(1,100)
startGame = True

print("welcome to the Number guessing Game!")
print("I'am thinking of a number betwee 1 and 100.")
level=input("Choose a difficult. Type 'easy' or 'hard':").lower()

   
while startGame:
    if(level == 'easy'):
        print(f"You have {easy_attemp} remaining to guess the number")
        guess=int(input("Make a guess:"))
        print(myNumber,guess)  
        if(easy_attemp==0):
            startGame=False
            print("You lose")    
        elif(myNumber > guess):            
            easy_attemp-=1
            print("Too low")
            print("Guess again")
            # print(f"You have {easy_attemp} remaining to guess the number")            
        elif(myNumber < guess):            
            easy_attemp-=1
            print("Too high")
            print("Guess again")
            # print(f"You have {easy_attemp} remaining to guess the number")
            guess=input("Make a guess:")
        
        elif(myNumber ==guess):
            print("You won!")
            startGame=False
    if(level == 'hard'):
        print(f"You have {hard_attemp} remaining to guess the number")
        guess=int(input("Make a guess:"))
        print(myNumber,guess)  
        if(hard_attemp==0):
            startGame=False
            print("You lose")    
        elif(myNumber > guess):            
            hard_attemp-=1
            print("Too low")
            print("Guess again")
            # print(f"You have {easy_attemp} remaining to guess the number")            
        elif(myNumber < guess):            
            hard_attemp-=1
            print("Too high")
            print("Guess again")
            # print(f"You have {easy_attemp} remaining to guess the number")
            guess=input("Make a guess:")
        
        elif(myNumber ==guess):
            print("You won!")
            startGame=False
   

            




