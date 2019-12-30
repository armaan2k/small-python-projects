'''
Name: Armaan Merchant
program description: A game that scores users based on randomly generated dice throws and gives them a total in the end
'''

#imports the random library from python into the code
import random

#defining the function that runs most of the game
def dice():
    print("Welcome to the Dice Game! You will recieve points for rolling doubles, a total of 7 or rolling a 6!\nLets begin playing!!!")
    keep_going = 'Y'
    score = 0
    #A while loop to generate 2 random numbers and add it to the variable score based on the criteria of the game
    while keep_going == "Y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        #if statements to update the score based on the random rolls of the two dice
        if (dice1 + dice2) == 7:
            score = score + 2
        elif dice1 == 6:
            score = score + 4
        elif dice2 == 6:
            score = score + 4
        elif dice1 == dice2:
            score = score + 10

        #prints out the values for the user so they can see the dice values and running score
        print ('\nDice 1 is', dice1)
        print ('Dice 2 is', dice2)
        print('Your total score is', score)

        #define a variable to use in the while loop
        keep_going = 'Z'

        #a while loop to ask the user if they want to keep playing the dice game
        while keep_going != 'N' and keep_going != 'Y':
            keep_going = input("If you wish to keep playing type 'Y' otherwise type 'N' to end the game: ")
    print('\nThanks for playing the Dice Game!!! You finished with a total score of', score)

#calls the function dice to start the program
dice()