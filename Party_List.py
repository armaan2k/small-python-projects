'''
Name: Armaan Merchant
program description: A program that takes 2 lists, total friends and people invited to a party, and creates a third list that shows
all the people not invited to the party
'''

#the three variables used in the code
list_friends = ['Alice','Nob','Joe','Sam','Kate']
list_invited = ['Alice','Nob','Joe']
list_new = []

#for loop to make list_new to be the same as list_friends without being connected to each other e.g list_new = list_friends wont work with the code
for y in range(len(list_friends)):
    list_new.append(list_friends[y])

#for loop to remove the people who are invited (list_invited) from list_new to give you the list of people not invited to the party
for x in range(len(list_friends)):
    if list_friends[x] in list_invited:
        list_new.remove(list_friends[x])

#tells the user who is not invited
print('Here is a list of people not invited to Alices party:\n', list_new)