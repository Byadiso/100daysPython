# print('Welcome to the rollecoaster!')
# heigh = int(input('what is your heigh in cm?'))

# if heigh >= 120:
#     print('You can rid the rollercoaster!')
# else:
#     print("Sorry you have to grow taller before you can ride")

# num =int(input("Type your number\n"))

# isEven = num % 2 == 0

# if isEven:
#     print('It is an even number')
# else:
#     print('It is an odd number')



# calculation of BMI

#leap year 


# year = int(input('Type the year to check for this leap year hypothesis\n'))

# if year % 4 == 0 & year % 100 == 0 & year % 400 == 0:
#     print("leap Year")
# else:
#     print('It is not a leap year')


print("Find hidden treasure")
choice = input("Where do you want to go?, 'Right' or 'Left'\n").lower()

if choice == 'left':
    choice2= input("Do you want to go by swim or Wait a boat? ").lower()
    if choice2 == 'wait':
        print("Your boat is ready")
        print("You are heading to an island")
        print("You have reached to the  island")

        choice3=input("There are 3 doors on this island with 3 colors.\nWhich door will you enter?\nThe one with Red, blue, green? ").lower()
        if choice3=="green":
            print("You find your hidden treasure! Congratulations, you won!")
        else:
            print("You went into a room full of beasts, you loose. Game over")

    else:
        print("crocodiles jumped over you, Game Over")

else:
    print("You fall into a hole, Game Over")