# Day 8
# Hangman project


# def gret(name):
#     print(f"Hello {name}")
#     print(f"How are you today  {name}")
#     print(f"Bye my dear friend {name}")

# gret("Desire")

# import math

# def paint_calc(height, width, coverage):
#     numberofCan = math.ceil((height * width)/coverage)

#     print(f'You will need {numberofCan} of paint')

# paint_calc(3,2,5)


# # Check a prime number

# n=int(input("Check your number\n"))

# def isPrime(number):
#     isPrime= True
#     for i in range(2,number):
#         if( number % i ==0):
#            isPrime= False
#     if isPrime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
# isPrime(n)


# Caesar Ciphar

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type  the shift number: \n"))

text = "ZULU"
shift = 5

print(f"starting message is {text}")


def encrypt(text, shift):
    encodeMessage = ' '
    alphabetToEncrypt = list(text)

    for letter in alphabetToEncrypt:

        if letter in alphabet:
            thatLetterIndex = alphabet.index(letter)
            if thatLetterIndex == len(alphabet)-1:
                thatLetterIndex = -1
            afterEncode = thatLetterIndex + shift

            thatLetter = alphabet[afterEncode]
            encodeMessage += thatLetter

    print(f"Encrypted message is {encodeMessage}")
    return encodeMessage


message = encrypt(text, shift)

print(f"{message} is the message encrypted")


def decode(message, shift):
    encryptedMessage = ""
    alphabetToDecode = list(message.upper())

    for letter in alphabetToDecode:

        if letter in alphabet:
            thatLetterIndex = alphabet.index(letter)

            afterEncode = thatLetterIndex - shift

            thatLetter = alphabet[afterEncode]
            encryptedMessage += thatLetter

    print(f"Decrypted message is {encryptedMessage.upper()}")


decode(message, shift)
