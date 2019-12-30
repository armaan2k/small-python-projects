'''
Name: Armaan Merchant

Programme simulates a basic calculator with 4 functions and an end option
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
    #An while loop that makes sure you can't divide by 0 and asks the user for another number
    while y == 0:
        print ("Sorry, you can't divide by 0")
        y = float(input("Please re-enter the second number you want to divide: "))

    if y != 0:
        print (x, '/', y, '=', x/y)

#multiply function
def multiply():
    x = float(input("enter the first number you want to multiply: "))
    y = float(input("enter the second number you want to multiply: "))
    print (x, '*', y, '=',  x * y)

#Function main calls on the other function according to the users choice
def main():
    #asks user to call the relevant function
    choice = input("Please enter the appropriate function.\n'A' for addition\n'S' for subtraction\n'D' for divide\n'M' for multiply\n'E' to end the program\nEnter your choice: ")
    while choice != 'E':
        if choice == 'A':
            add()
        elif choice == 'S':
            subtract()
        elif choice == 'D':
            divide()
        elif choice == 'M':
            multiply()
        choice = input('Enter your choice of function: ')
    if choice == 'E':
        print('Program terminated')

#calls on the function 'main' to run
main()

#end of program
