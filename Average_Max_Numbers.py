'''
Name: Armaan Merchant
program description: takes the users numbers and finds the average and maximum number from those numbers
'''


#puts the users numbers into a list
def num_in_list(numb,list1):
    if numb != 999:
        list1.append(numb)
        return list1
    elif numb == 999:
        return list1

#takes the numbers in the list and calulates and average
def average(Mylist):
    if len(Mylist) != 0:
        total = 0
        for i in Mylist:
            total += i
        mean = total/(len(Mylist))
        print('\nThe average is', mean)
    elif len(Mylist) == 0:
        print('\nThe average is 999')

#finds the max number from the  list
def maximum(Mylist):
    if len(Mylist) != 0:
        maxNum = max(Mylist)
        print('\nThe maximum number is', maxNum)
    elif len(Mylist) == 0:
        print('\nThe maximum number is 999')


def menu(list1):
    #defining choice so its can be used
    choice = 0
    #while loop so the program will keep running until the user inputs 3 as their choice
    while choice != 3:
        print('\n1) Find the average:\n2) Find the maximum number\n3) Exit\n')
        choice = int(input('Ok, what would you like to do (enter the corresponding number): '))
        if choice == 1:
            average(list1)
        elif choice == 2:
            maximum(list1)
        elif choice == 3:
            print('Thanks for playing!')
            return





def main():
    print('Hello! Please enter some numbers. When you are finished, enter 999\n')
    Mylist = []
    num = 0
    while num != 999:
        num = int(input('Enter a number: '))
        Mylist = num_in_list(num,Mylist)

    menu(Mylist)

main()
