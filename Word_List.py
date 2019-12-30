'''
Name: Armaan Merchant
Program description: This program does all kinds of cool stuff with lists. First it edits the list to remove 'Bad' words
and then allows the user to find out information about the words in the list unit the user decides to end the program
'''

import urllib.request #this loads a library you will need - put this at top of file.
import collections

def readWordList():
    response = urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000")
    html = response.read()
    data = html.decode('utf-8').split("\n")
    return data

#creates a variable to hold the list of words
words = readWordList()

#removes all empty strings from the list, e.g list[10000] is an empty string which disrupts the some of the list functions
while '' in words:
    words.remove('')

#a new varible that will be a copy of words so that when the variable 'words' is changed it doesnt affect the range of the loop
words_new = []

#creates a variable of a list of the alphabet to be used to identify letters in a list
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#creates a varible with an empty list that will be filled with words of just repeated letters
repeats = []

#defines a function that removes the words with repeated letters
def cleanup():

    #a for loop that appends the words from 'words' to 'words_new' because if I try create a copy by setting the variables equal to each other,
    #a change to one varible will also result in a change to the other creating problems with the range of my loops
    for x in range(len(words)):
        words_new.append(words[x])

    #a for loop that fills the empty list repeat with the probable repeated 'Bad' words
    # (assuming that the repeated 'words' dont have more than 5 consecutive repeated letters)
    for i in range(len(alphabet)):
        for x in range(5):
            repeats.append(alphabet[i]*(x+1))

    #a for loop that checks if the 'Bad' words are in the list and removes then if they are
    for i in range(len(words)):
        if words[i] in repeats:
            words_new.remove(words[i])


def userinteraction(words_new):

    #asks the user for their input
    choice = int(input('\nPlease choose from the following options\n'
                   '"1" to ask if a word is in the list\n'
                   '"2" to ask how many words of length n are in the list, n being a number of your choice\n'
                   '"3" to find out how many words begin with a letter of your choice\n'
                   '"4" to quit the program\n'
                   'Please enter your choice: '))

    #a while loop to make sure that the program doesn't end if the user enters and invalid entry
    while choice < 1 or choice > 4:
        print('\nThat is not a valid entry!')
        choice = int(input('\nPlease choose from the following options\n'
                       '"1" to ask if a word is in the list\n'
                       '"2" to ask how many words of length n are in the list, n being a number of your choice\n'
                       '"3" to find out how many words begin with a letter of your choice\n'
                       '"4" to quit the program\n'
                       'Please enter your choice: '))

    #if the users choice was 1 it asks the user for their input and using an if statement, checks if word is in the list
    if choice == 1:
        choice1 = input('\nEnter the word you wish to check for: ')
        if choice1 in words_new:
            print(choice1, 'is in the list')
        else:
            print(choice1, 'is not in the list')

        #calls the function again
        userinteraction(words_new)

    #if the users choice was 2 it asks for the users input
    elif choice == 2:
        choice2 = int(input("\nEnter the 'n' value to find how many words of length 'n' are in the list: "))
        count = 0

        #for loop to go through all the words in words_new. the if statement checks if the length of the word matches
        #the users input and if so it adds to the  count
        for i in words_new:
            if choice2 == len(i):
                count += 1
        print('There are', count, 'words with length', choice2, 'in the list')

        #calls the function again
        userinteraction(words_new)

    elif choice == 3:
        choice3 = input('\nTo find how many words begin with a letter, enter your chosen letter: ')
        count2 = 0
        for i in words_new:
            if choice3 == i[0]:
                count2 += 1
        print('There are', count2, 'words that start with the letter', choice3, 'in the list')

        #calls the function again
        userinteraction(words_new)

    #ends the program
    elif choice == 4:
        print('\nGoodbye')
        return

#defines the function main which calls cleanup() and userinteraction()
def main():
    cleanup()
    userinteraction(words_new)

#starts the program by calling main
main()
