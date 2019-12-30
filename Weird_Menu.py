'''
Name: Armaan Merchant

Programme decription: Welcomes the user and asks the user to pick 1 of 3
options. Each option will trigger a response from the programme.
'''

def menu():
        
    #interative greeting and promt for options
    name = input ('Hello! Welcome to my progam. Please enter your name: ')
    print ('Hello,', name)
    option = int(input (' Please choose one of the following options: \n 1) Sing me a song\n 2) Tell me a joke\n 3) Draw me a picture\n Enter your option here: '))


    #Tell user the integer is invalid
    if option <= 0: print ("Sorry that is not an option")
    if option >= 4: print ("Sorry that is not an option")

    #acknowledging the persons choice
    if option == 1 or option == 2 or option == 3: print (" you chose option #", option)

    #options 1 to 3
    if option == 1: print ("LA LAAA LAAA LAA!!!")
    if option == 2: print ("Why do the French like to eat snails so much?\n...\nThey can't stand fast food.")
    if option == 3: print ("Sorry I cant draw but here is an emoji :p ")
    if option == 1 or option == 2 or option == 3: print ("Thank you for playing. Come again soon!")

#run the function
menu()

#end of code
