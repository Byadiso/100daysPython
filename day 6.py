# # print('Welcome to the rollecoaster!')
# # heigh = int(input('what is your heigh in cm?'))

# # if heigh >= 120:
# #     print('You can rid the rollercoaster!')
# # else:
# #     print("Sorry you have to grow taller before you can ride")

# # num =int(input("Type your number\n"))

# # isEven = num % 2 == 0

# # if isEven:
# #     print('It is an even number')
# # else:
# #     print('It is an odd number')



# # calculation of BMI

# #leap year 


# # year = int(input('Type the year to check for this leap year hypothesis\n'))

# # if year % 4 == 0 & year % 100 == 0 & year % 400 == 0:
# #     print("leap Year")
# # else:
# #     print('It is not a leap year')

# Day 3

# print("Find hidden treasure")
# choice = input("Where do you want to go?, 'Right' or 'Left'\n").lower()

# if choice == 'left':
#     choice2= input("Do you want to go by swim or Wait a boat? ").lower()
#     if choice2 == 'wait':
#         print("Your boat is ready")
#         print("You are heading to an island")
#         print("You have reached to the  island")

#         choice3=input("There are 3 doors on this island with 3 colors.\nWhich door will you enter?\nThe one with Red, blue, green? ").lower()
#         if choice3=="green":
#             print("You find your hidden treasure! Congratulations, you won!")
#         else:
#             print("You went into a room full of beasts, you loose. Game over")

#     else:
#         print("crocodiles jumped over you, Game Over")

# else: 
#     print("You fall into a hole, Game Over")




# Day 4



# import random



# # print(randomInt)

# name = ['Desire','Patrick','Eric','Olivier','Raissa']

# # print(name)
# rangeList=int(len(name))


# randomInt= random.randint(0,rangeList-1)

# choice=name[randomInt]

# print(f"{choice} will buy for us food today")



# project is Rock Paper Sciessors

# import random

# shape = ["rock","paper","scissors"]
# randomInt= random.randint(0,len(shape)-1)

# computer= shape[randomInt]

# user= input("Type your choice between Rock, Paper, Scissors\n").lower()

# print( user,computer)

# if( user =='rock' and computer== 'paper'):
#     print("User win")
# elif (user =='paper' and computer and 'scissors'):
#     print("Computer win")
# elif(user =='paper' and computer== 'paper'or user =='scissors' and computer== 'scissors' or user =='rock' and computer== 'rock'):
#     print("it is a drow let try again")
# else:
#     print("User win")


# Day 5

# Password generator 

# import random

# letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# numbers =['0','1','2','3','4','5','6','7','8','9']
# specialCharacters= ['@','#','<','>','$','%','&','*','(',')','=','+','-','!']

# print("Welcome to Py password Generator")
# ChoiceLetters=int(input("How many characters do you want for your password?\n"))
# ChoiceNumbers=int(input("How many numbers do you want for your password?\n"))
# ChoiceSpecialChar=int(input("How many special character do you want for your password?\n"))

# password=[]

# for letter in range(1,ChoiceLetters+1 ):    
#     password.append(random.choice(letters))

# for number in range(1,ChoiceNumbers+1 ):    
#     password.append(random.choice(numbers))
# for special in range(1,ChoiceSpecialChar+1 ):    
#     password.append(random.choice(specialCharacters))

# newPassword= ''

# for char in password:
#     newPassword += char

# print(f"Your Password is {newPassword}")




# Day 6

# Loops  

# For loop & while loop


# for loop when we care about the element in the loop list

# While loop when we don't care about the element


# Reeborg's world   solve a maze problem


