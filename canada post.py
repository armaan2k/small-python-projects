'''
Name: Armaan Merchant

Program description: A program that processes user inputed data in order to tell them the price of their package
'''
print("Welcome to Canada Post!\n")

#Function for running price of letters
def letter():
    if location == 'Canada':
        print("Price = $1.00\n")
    if location == 'International':
        print("Price = $1.75\n")

#Fuction for running price of parcels
def parcel():
    if weight < 1 and location == 'Canada':
        print("Price = $5.50\n")
        
    if weight < 1 and location == 'International':
        print("Price = $8.75\n")

    if weight >= 1 and weight <= 5 and location == 'Canada':
        print("Price = $10.00\n")
        
    if weight >= 1 and weight <= 5 and location == 'International':
        print("Price = $18.75\n")

    if weight > 5 and location == 'Canada':
        print('Price = $25.25\n')

    if weight > 5 and location == 'International':
        print('Price = $40.75\n')

def main():

    #making the variable global so the other functions can use it
    global weight
    weight = float(input("Enter the weight of your package in kilograms: "))
    if weight < 0:
        print("Invalid weight\n")
        
    #making the variable global so the other functions can use it    
    global location
    location = input("Is your package being delivered to Canada or an International destination?\nEnter 'Canada' or 'International' : ")
    if location != 'Canada' and location != 'International':
        print('Invalid location\n')
        
    #making the variable global so the other functions can use it    
    global item_type
    item_type = input("Is your item a parcel or letter?\nEnter 'Letter' or 'Parcel' : ")
    if item_type != 'Letter' and item_type != 'Parcel':
        print('Invalid item type\n')

    #calls the function depending on the item type    
    if item_type == 'Letter':
            letter()
    if item_type == 'Parcel':
            parcel()
            
    #Asks user if they want to find the price of a new package and runs the main function again if they do
    new_item = input("Do you wish to mail another package?\nEnter 'Yes' or 'No' : ")
    if new_item == 'Yes':
        print('')
        main()
    else:
        print("Thank you choosing Canada Post")
              
main()
