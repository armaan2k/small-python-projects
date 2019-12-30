'''
Name: Armaan Merchant

Program description: A Text based game that allows the user to pick options in order to get a varied story line and different endings
'''

#imports the time library from python into the code, this allows me you space my text with a time delay
import time

def start():
    #adds a 2 second time delay to the next sentence to make sure the text pops up as the reader is reading it rather than all popping up at once
    time.sleep(2)
    print("\nOn the street ahead of you, you see a crowd that has formed a large ring around something, the crowd is cheering and shouting. To your left there is a 24/7 convience store")
    print("Do you want to go AHEAD or go LEFT?")
    choice = input("Choose 'A' for AHEAD or 'L' for LEFT: ")
    #if statement to call the fight or store function of the story depending on the readers choice
    if choice == 'A':
        fight()
    elif choice == 'L':
        store()
    else:
        #A statement to tell the user the entry was not correct
        print('That is an invalid entry')

#fucntion for fight scene/location
def fight():
    print("\nYou push through the crowd to see whats happening. You come across an abnormal street fight...")
    time.sleep(2)
    print("There are two dwarfs, one wielding a long styrofoam pool noodle and the other holding a large wooden spoon")
    time.sleep(2)
    print("People are throwing money forward and placing bets")
    print("Do you choose to bet on the fight or stop the fight before someone gets hurt?")
    choice = input("Choose 'B' to bet or 'S' to stop the fight : ")
    if choice == 'B':
        #A new set of options based on the pervious choice to bet 'B'
        print("You chose to place a bet!")
        bet = input("Who do you bet on?\n'P' for pool noodle dwarf and 'S' for wooden spoon dwarf : ")
        if bet == 'P':
                  print("You place a $5 bet...\nThe dwarf wielding the pool noodle clipped the other dwarfs foot causing him to fall over.")
                  time.sleep(2)
                  print("Seeing his chance he relentlessly batters the other dwarf to a bloody pulp with the pool noodle!!!\n The crowd clears and you recieve your winnings")
                  building()
        elif bet == 'S':
                  print("You place a $5 bet...\nThe dwarf holding the large wooden spoon uses brute force to knock away the pool noodle and bludgeons the other dwarf")
                  time.sleep(2)
                  print("The fight is over and the crowd clears. You recieve your winnings")
                  building()
        else:
            print("invalid entry")
    elif choice == 'S':
        print("You attempt to break up the fight but in a bout of rage the dwarfs turn on you!")
        time.sleep(2)
        print("Covered in scratches and bruises, you barely make it out of the crowd")
        time.sleep(2)
        print("As you walk, shouts of joy and outrage indicate the fight is over")
        building()
    else:
        print('That is an invalid entry')

#function for store location
def store():
    print("\nYou walk into the convience store to buy adult diapers.")
    time.sleep(2)
    print("While waiting in line to pay you notice the elderly woman in front of you doesn't have enough money to pay for her groceries")
    time.sleep(2)
    print("Do you choose to cover her bill or pay for your diapers and leave?")
    choice = input("Choose 'C' to cover her bill or 'P' to pay for your diapers and leave: ")
    if choice == 'C':
        print("The elder woman thanks you and offers you a werthers original sweet")
        time.sleep(2)
        print('You graciously except the sweet and proceed to consume it.')
        time.sleep(2)
        print("However in your rush of euphoria due to your charitable act you forgot to check what the sweet contained.")
        time.sleep(2)
        print("Realising that you are deathly allegeric, you turn pale at the taste of caramel and spit the sweet out into the elderly womans open mouth")
        time.sleep(2)
        print("You stumble out of the store, your face swelling are turning an unhealthy plum colour")
        start()
    elif choice == 'P':
        print("The cashier gives you a strange look and smirks as you pay for your adult diapers")
        print("You walk back out to the street")
        start()
    else:
        print('Invalid entry')

#function for building location     
def building():
    print("\nAfter the crowd disperses you are close to your apartment and walk to the building")
    time.sleep(2)
    print("You enter the lobby. In the lobby there is a drunk seemingly homeless man dressed as santa claus and he is making a ruckus!")
    time.sleep(2)
    print("Do you confront Santa or call for the elevator")
    choice = input("Enter 'S' for confronting Santa or 'E' for calling the elevator : ")
    if choice == 'S':
        print("You tap Santa on the shoulder and he screams 'GO AWAY IM ALL OUT OF PRESENTS!!!'")
        time.sleep(2)
        print("Terrified by the wild look in Santas eyes you back away and call the elevator")
        elevator()
    elif choice == 'E':
        print("You walk up to the elevator and press the button")
        elevator()
    else:
        print('Invalid entry')

#function for elevator location
def elevator():
    print("\nDING! The elevator dings opens to three identical looking men in black suits and sunglasses")
    time.sleep(2)
    print("You walk in and stand uncomfortably between the 3 men. You push the button for your floor and wait as the old elevator creeps upwards")
    time.sleep(2)
    print("Do you choose to make small talk or say nothing")
    choice = input("Enter 'S' for small talk and 'N' for say nothing : ")
    if choice == 'S':
        print("You ask the three men how their evening was")
        time.sleep(2)
        print("They turn their head and give you blank looks. Turn away and dont say anything...")
        time.sleep(2)
        print("You probe them more by asking if they were ok but once again you get no response so you give up")
        appartment()
    elif choice == 'N':
        print("You just stand around until the elevator slowly reaches its destination")
        appartment()
    else:
        print('Invalid entry')

#function for appartment location
def appartment():
    print("\nYou quickly exit the elevator to get away from the silent awkward men and start to open your apartment door")
    time.sleep(2)
    print("As you start to get your keys out you notice the the door is cracked open!")
    time.sleep(2)
    print("From the darkness of your appartment you hear an ominous two tone tune playing on the grand piano")
    time.sleep(2)
    print("Do you choose to enter the appartment or run away?")
    choice = input("Enter 'E' to enter or 'R' to run away : ")
    if choice == 'E':
        room()
    #elif statement for ending 1 if user picks 'R'
    elif choice == 'R':
        print("You choose to run away and never turn back! There was simply too much going on tonight and your mind simply snapped!")
        time.sleep(2)
        print("You live the rest of your life in a motel in mexico. You haven't lost your mind but you have never been yourself since that day")
        print("THE END")
    else:
        print("invalid input")

#function for ending 2
def room():
    print("You enter the room cautiously and call 'Hello?' into the darkness")
    time.sleep(2)
    print("The lights suddenly turn on and you are startled! You are grabbed from behind and as a bag is forced over your head you catch a glimps of the men in suits!")
    time.sleep(2)
    print("You are seated on a small stool in the living room as the music comes to an abrupt stop")
    time.sleep(2)
    print("A gruff voice says 'You are fortunate enough to have been chosen as the first trial for project antelople due to your unique physique'")
    time.sleep(2)
    print("'Thank you for serving your country'")
    time.sleep(2)
    print("You feel a sharp prick in your neck and slowly lose consciousness")
    print("THE END")

#The function main to call start in order to start the story
def main():
    print("You are walking down the street on your way home on a cold and dark winter night")
    start()

#calls main
main()
