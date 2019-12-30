'''
Name: Armaan Merchant
Program description: a program that simulates the crown and anchor game
'''

#random is used to simulate the wheel spin using randomly generated numbers
import random

#takes user information for important variables such as the symbols for the bet and the bet amount
def bets(players,player):

    #ask user is they wish to make a bet
    Y_or_N = input('\nDo you wish to bet this round?\nEnter "Y" for yes or "N" for no: ')
    #a while loop to prevent an invalid entry and prompts the user for another entry
    while Y_or_N != 'Y' and Y_or_N != 'N':
        print('\nSorry that is an invalid entry')
        Y_or_N = input('Do you wish to bet this round?\nEnter "Y" for yes or "N" for no: ')

    #if the users doesn't place a bet, we still have to create the variables used in the code so it set to 0
    if Y_or_N == "N":
        symbol = 0
        bet = 0

    elif Y_or_N == "Y":

        #gets the  symbol the user wishes to  bet  on and uses a while loop to prevent invalid entries
        symbol = int(input("\nWhat symbol are you betting on?\n'1' for Hearts\n'2' for Diamonds\n'3' for Spades\n'4' for Clubs\n'5' for Crowns\n'6' for Anchors\nEnter the number representing your chosen symbol: "))
        while symbol != 1 and symbol != 2 and symbol != 3 and symbol != 4 and symbol != 5 and symbol != 6:
            print('\nSorry that is an invalid entry')
            symbol = int(input("What symbol are you betting on?\n'1' for Hearts\n'2' for Diamonds\n'3' for Spades\n'4' for Clubs\n'5' for Crowns\n'6' for Anchors\nEnter the number representing your chosen symbol: "))

        #gets the bet amount from the user, a $0 option is given so if a user says they wish to bet, but have no money, they can realise their mistake rather than being repeatedly shamed by beinng told they dont have enough money
        bet = int(input('\nYou may bet $0, $1, $2, $5 or $10\nEnter the amount you wish to bet: '))
        #while loop to prevent invalid entries
        while bet != 0 and bet != 1 and bet != 2 and bet != 5 and bet != 10:
            print('\nSorry that is an invalid amount')
            bet = int(input('You may bet $0, $1, $2, $5 or $10\nEnter the amount you wish to bet: '))

        #while loop to make sure the user doesn't enter a bet amount they cant afford to lose (more than they have)
        while (players[player] - bet) < 0:
            print('\nSorry you dont have enough money to make that bet')
            bet = int(input('You may bet $0, $1, $2, $5 or $10\nEnter the amount you wish to bet: '))
            while bet != 0 and bet != 1 and bet != 2 and bet != 5 and bet != 10:
                print('\nSorry that is an invalid amount')
                bet = int(input('You may bet $0, $1, $2, $5 or $10\nEnter the amount you wish to bet: '))

    #returns 2 important variables
    return (symbol,bet)

#simulates the spin of the wheel
def spin():
    outcome = []
    #for loop to append 3 random numbers to an empty list
    for x in range(3):
        outcome.append(random.randint(1,6))
    return outcome

#calulates and updates players scores aswell as informing players of their winnings
def player_winnings(symbol,bet,outcome,player,players):
    if symbol in outcome:
        new_score = (players[player]) + bet*(outcome.count(symbol))
    else:
        new_score = players[player] - bet

    #deletes the players previous score in the list and replaces it with the updated version
    del players[player]
    players.insert(player,new_score)

    #informs players about their winnings that round
    if 6 in outcome and outcome.count(symbol) == 3:
        print('Winner on Anchors -- Ahoy!!!!')
    print('\nPlayer', player + 1, 'won $', (bet*(outcome.count(symbol))))


def files(players):
    #creates a file called game_results.txt in writing mode. writes a record of the players scores
    with open('game_results.txt', 'a') as file:
        for x in range(len(players)):
            file.write('Player ')
            file.write(str(x+1))
            file.write(' $')
            file.write(str(players[x]))
            file.write('\n')



def main():

    #the start of  the  game which asks the user how many people wish to play this game and puts that many players into a list with a starting amount of $10 using a for loop
    player_entry = int(input('Enter the number of players participating: '))
    players = []
    for x in range(player_entry):
        players.append(10)
    rounds = 0

    print('Everyone starts with $10! Good luck!')

    #this while loops runs until everyone has lost their money... hehe
    while sum(players) > 0:

        #updates the round number and prints it
        rounds += 1
        print('\nROUND:', rounds)

        #writes the round number into the file 'game_results.txt'
        with open('game_results.txt', 'a') as file:
            file.write('Round ')
            file.write(str(rounds))
            file.write('\n')

        #for loop for simulate multiple players playing
        for x in range(len(players)):
            player = x
            print('Player', x+1, 'turn:')

            #runs the function bets and collects the results in a tuple to be used
            bet_result = bets(players,player)

            #runs the spin function and saves the outcome as a variable
            spin_result = spin()

            #runs the player_winnings function and passes the approriate variables
            player_winnings(bet_result[0],bet_result[1],spin_result,player,players)

        #lets the players know their current total scores at the end of the round using a for loop to inform each player
        print('\nRound', rounds, 'results:')
        for x in range(len(players)):
            print('Player', x+1, 'current total is $', players[x])

        #runs the files function that adds the players and their scores to the file after the round has been written
        files(players)

    #just being polite
    print('\nThanks for playing!')

#calls main...
main()
