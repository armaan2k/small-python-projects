'''
Name: Armaan Merchant
program description: 4 functions that solve problems using recursion and a menu function to test them
'''

#function 1, takes the number of the user as the input and prints them backwards using recursion
def printDigits(digits):
    #base case is when digits = 0
    if digits != 0:
        #prints the integer on the end of the number
        print(digits % 10)
        #calls digits again and gets rid of the integer at the end when it passes it again
        printDigits(digits//10)

#function 2, takes a number from the user as the input and returns true if the number is even(this is the recursive version)
def even_then_true(number):
    #changes negative numbers to positive ones so it works in the program
    if number < 0:
        number = number*(-1)
        #runs the function with the postive integer as the parameter
        return even_then_true(number)
    #for the even case it returns true
    elif number == 0:
        return True
    #for the odd case it returns false
    elif number == 1:
        return False
    else:
        #call the functions again but reduces the number by 2 so it remains odd or even
        return even_then_true(number-2)

#function 3, takes a number from the user and returns true if it is even(this is the non-recursive version)
def even_non_recursive(number):
    stop = ''
    #while loop to reach desired conditional, unnecessary stop conditional due to return
    while stop != 'Stop please omg in the name of god AHHHH he has a knife!':
        #changes a negative number to a positive
        if number < 0:
            number = number*(-1)
        #even case returns true
        elif number == 0:
            return True
        #odd case returns false
        elif number == 1:
            return False
        #reduces number by 2
        else:
            number = number - 2


#function 4, prints 1 to n lines of asterisks with 1 to n asterisks. Takes users input for n parameter
def asterisks_art(n):
    #reduces n recursivly until n = 1 and then prints out the asterisks from 1 to n
    if n >= 1:
        #calls the function again with n-1
        asterisks_art(n-1)
        print(n*'*')

#function 5, prints the value of the user given exponential with parameters for number and power
def exponential(number,power):
    #multiplies the number by itself until the power reaches 0
    if power == 0:
        return 1

    else:
        #calls the fuction again with 1 less for power
        return number*(exponential(number,power-1))


def main():
    #defines choice for the while loop
    choice = ''

    #while loop to keep the menu going until the user wishes to exit
    while choice != 'exit':

        print('\nTo exit the program please enter "exit"')
        print('Function 1: Prints the integer you enter in backwards order')
        print('Function 2: Returns true if your chosen number is even(recursive)')
        print('Function 3: Returns ture if your chosen number is even(non-recursive)')
        print('Fucntion 4: Lines of asterisks are printed depending the number of lines you choose')
        print('Function 5: Calulates your chosen exponential')

        #the user input for choice
        choice = input('\nPlease choose 1 of the 5 functions to run. Enter the appropriate number: ')

        if choice == '1':
            data1 = int(input('Enter the number you wish to use: '))
            printDigits(data1)

        elif choice == '2':
            data1 = int(input('Enter the number you wish to use: '))
            print(even_then_true(data1))

        elif choice == '3':
            data1 = int(input('Enter the number you wish to use: '))
            print(even_non_recursive(data1))

        elif choice == '4':
            data1 = int(input('Enter the number you wish to use: '))
            asterisks_art(data1)

        elif choice == '5':
            data1 = int(input('Enter the number you wish to raise to a power: '))
            data2 = int(input('Enter the power you wish to use in the exponential: '))
            print(exponential(data1,data2))

    #indicates the program has successfully ended
    print('Thanks...BYE!')

main()