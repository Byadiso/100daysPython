# Day 10
# calculator project


""" Desire
is doing great"""


# print("Yes now we know about Docstring")


# def outer_function(a,b):
#     def inner_function(c,d):
#         return c + d
#     return inner_function(a,b)
# result = outer_function(5,10)
# print(result)

def add(num1, num2):
    num1 += num2
def divide(num1, num2):
    num1 /= num2

def multiply(num1, num2):
    num1 *= num2

def substract(num1, num2):
    num1 -= num2


operations ={
    "+":add,
    "-":substract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("what's is the first number? :"))

for symbol in operations:
    print(symbol)
    
operation_symbol = input("Pick an operation from line above :")

num2 = int(input("what's is the second number? :"))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)






