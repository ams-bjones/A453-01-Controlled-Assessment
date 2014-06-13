currencies = ["Pounds", "Dollars", "Yen", "Euros"]
#This states the available currency's.
Pounds = 'Pounds'
Dollars = 'Dollar'
Yens = 'Yen'
Euros = 'Euros'
#This sets the variable names for the currency's (Lines 3 to 6)
rates = [1, 2, 3, 4]
#This makes a variable called 'rates' and has the currency exchange rates stored in the variable
print ("Welcome to the Currency Converter, please enter your name")
#Welcomes the user to the converter and asks for the user to enter their name
name = raw_input ("name: ")
#The system allows a value to be entered into the space next to 'name:'
print ("Hi there {0}!".format(name))
#The system says 'Hi there !' In the space between the exclamation mark and the word 'there' is where the value is added. 
#The system will allow any value to be entered, even numbers.  !' In the space between the exclamation mark and the word 'there'

print ("Pound", rates[0])
print ("Dollars", rates[1])
print ("Euro", rates[2])
print ("Yen", rates[3])

choice = input("Please enter your choice: ")

if choice == rates[0]:
    print ("You have selected Pounds")

if choice == rates[1]:
    print ("You have selected Dollars")
    
if choice == rates[2]:
    print ("You have selected Euros")
    
if choice == rates[3]:
    print ("You have selected Yen")
    
converting = input("Please enter the sum you wish to convert in the currency you chose: ")

print ("Converted answer is,"[0]"Pounds, "[1]"Dollars, "[2]"Euros, "[3]"Yens")
print ("Thank you for using the money converter :)")

