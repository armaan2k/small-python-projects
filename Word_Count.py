'''
Name: Armaan Merchant
Program description: This wacky program formats a string to be lower case and without punctuation in order to count the times a word is repeated
'''

#the passage of text to use in the code
passage =   ("To be, or not to be, that is the question: "
            "Whether 'tis nobler in the mind to suffer "
            "The slings and arrows of outrageous fortune, "
            "Or to take Arms against a Sea of troubles, "
            "And by opposing end them: to die, to sleep "
            "No more; and by a sleep, to say we end "
            "the heart-ache, and the thousand natural shocks "
            "that Flesh is heir to? 'Tis a consummation "
            "devoutly to be wished. To die, to sleep, "
            "To sleep, perchance to Dream; aye, there's the rub, "
            "for in that sleep of death, what dreams may come, "
            "when we have shuffled off this mortal coil, "
            "must give us pause. There's the respect "
            "that makes Calamity of so long life: "
            "For who would bear the Whips and Scorns of time, "
            "the Oppressor's wrong, the proud man's Contumely, "
            "the pangs of despised Love, the Law’s delay, "
            "the insolence of Office, and the spurns "
            "that patient merit of the unworthy takes, "
            "when he himself might his Quietus make "
            "with a bare Bodkin? Who would Fardels bear, "
            "to grunt and sweat under a weary life, "
            "but that the dread of something after death, "
            "the undiscovered country, from whose bourn "
            "no traveller returns, puzzles the will, "
            "and makes us rather bear those ills we have, "
            "than fly to others that we know not of. "
            "Thus conscience does make cowards of us all, "
            "and thus the native hue of Resolution"
            "Is sicklied o'er, with the pale cast of Thought, "
            "And enterprises of great pitch and moment, "
            "with this regard their Currents turn awry, "
            "And lose the name of Action. Soft you now, "
            "The fair Ophelia? Nymph, in thy Orisons "
            "Be all my sins remembered.")

#a list with the possible punctuation as a string
punctuation = [".","!","@","#","$","%","^","&","*","-","{","}","[","]",",",";",":","'","?","<",">","/"]

#a for for loop to go through the types of punctuation and a while loop to remove  all the punctuation and replace it with an empty string
for x in range(len(punctuation)):
    while punctuation[x] in passage:
        passage = passage.replace(punctuation[x],'')

#2 variables with the all the lower case and upper case letters as strings in a list
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#a for loop to go through the upper case alphabet and a while loop to replace the upper case alphabet with the lower case equivalent
for x in range(len(upper_case)):
    while upper_case[x] in passage:
        passage = passage.replace(upper_case[x],lower_case[x])

#turns the passage(string) into a list with each word being a string in the list
passage = passage.split()

#creates an empty variable called repeat
repeat = []

#for loop to go through the words in the passage(list) and print out the words and how many times it is repeated
for x in range(len(passage)):
    #an if statement to make sure that the words has not been repeated and is not printed multiple times with its count
    if passage[x] not in repeat:
        print('Word:', passage[x], '\nWord count:', passage.count(passage[x]), '\n')
        #appends used words to the currently empty list repeat so that it prevents repeated words through the if statement and loop
        repeat.append(passage[x])


