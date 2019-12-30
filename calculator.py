'''
Name: Armaan Merchant
Program simulates a very basic calculator
'''

#add function
def add():
    x = float(input("enter the first number you want to add: "))
    y = float(input("enter the second number you want to add: "))
    print (x, '+', y, '=',  x + y)

#subtract function
def subtract():
    x = float(input("enter the first number you want to subtract: "))
    y = float(input("enter the second number you want to subtract: "))
    print (x, '-', y, '=',  x - y)

#divide function
def divide():
    x = float(input("enter the first number you want to divide: "))
    y = float(input("enter the second number you want to divide: "))
    #An if statement that makes sure you can't divide by 0
    if y == 0:
        print ("Sorry, you can't divide by 0")
    else:
        print (x, '/', y, '=',  x / y)
#multiply function
def multiply():
    x = float(input("enter the first number you want to multiply: "))
    y = float(input("enter the second number you want to multiply: "))
    print (x, '*', y, '=',  x * y)

#Function main calls on the other functions 1 by 1
def main():
    add()
    subtract()
    divide()
    multiply()

#calls on the function 'main' to run
main()

#end of program
