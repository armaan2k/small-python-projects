'''
name: armaan merchant
program description: a program that simulates a treasure hunt
'''
import urllib.request

#this reads the file from the url and splits each line in the text into a list
def readfile():
    url = "http://research.cs.queensu.ca/home/cords2/treasure.txt"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    list = html.splitlines()
    return list

#this goes through the list and checks if a string can be turned into a integer, if i can it is turned into an integer. it takes the unformated list as a parameter
def format_list(list1):
    for i in range(len(list1)):
        if list1[i].isdigit() == True:
            list1[i] = int(list1[i])
    return list1

#this runs the body of the game, takes the formated list and the knapsack(dictionary) as the parameter
def game(list, knapsack):
    #gives the user the initial choice of where to search
    print('\nChoose a number from 0 to', (len(list) - 1))
    choice = int(input('Enter your choice here: '))
    moves = 0

    #checks if the choice is in range of the list
    while choice <= (len(list) - 1):
        #checks if choice is an integer or string
        if type(list[choice]) == int:
            choice = list[choice]
            moves += 1
        #this is the actions if the choice is a string
        else:
            #checks if the key already exists
            if list[choice] in knapsack:
                knapsack[list[choice]] += 1
                moves += 1
                #lets the user know what they won
                print('Congradulations! This is what you found...', list[choice])
                # returns the updated knapsack and move count
                return (knapsack, moves)

            #adds the key to the list if it doesnt exist
            else:
                knapsack[list[choice]] = 1
                moves += 1
                # lets the user know what they won
                print('Congradulations! This is what you found...', list[choice])
                # returns the updated knapsack and move count
                return (knapsack, moves)

    #what happens if choice becomes an invalid index for the list.... they lose the game by the rules
    print('You lose! Your knapsack has been emptied!')
    moves = 0
    knapsack = {}
    #returns the updated knapsack and move count
    return (knapsack,moves)

#calulates the score by the rules. takes the knapsack(dictionary) and the variable moves are the parameter
def score(knapsack,moves):
    #the if and else statements check to see if the user has any of the items, if they dont the else statement sets the item to 0 so it can be used in the calculaltions
    if 'gold' in knapsack:
        gold = knapsack['gold']
    else:
        gold = 0

    if 'silver coins' in knapsack:
        silver = knapsack['silver coins']
    else:
        silver = 0

    if 'candy' in knapsack:
        candy = knapsack['candy']
    else:
        candy = 0

    if 'cell phone' in knapsack:
        phone = knapsack['cell phone']
    else:
        phone = 0

    #calculates the total score and gives user a breakdown of what they won
    total = gold*5 + silver*10 + candy*2 + phone*100 + moves
    print('')
    print(total, 'is your final score!\nHere is a break down for you: ')
    print('Gold:', gold)
    print('Silver coins:', silver)
    print('Candy:', candy)
    print('Cell phones:', phone)



#calls all the functions and welcomes the user
def main():
    print('Welcome to the treasure hunt! You can recieve all kinds of treasure such as gold, silver coins, candy and cell phones which you will collect in your knapsack!')
    print('But be careful... one false move and you could lose all your treasure!\nLet the hunt begin!')
    knapsack = {}
    list = readfile()
    list1 = format_list(list)
    plays = 'Y'
    #while loop to keep the user playing till they decide to exit
    while plays == 'Y':
        data = game(list1,knapsack)
        plays = input('\nTo keep playing enter "Y", other wise enter any key to exit\nEnter your response here: ')
    knapsack = data[0]
    moves = data[1]
    score(knapsack,moves)

#starts the program
main()