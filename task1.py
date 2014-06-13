currencies = ["GBP","USD", "EUR", "JPY"]
#This states the available currency's.
Pounds = 'Pounds'
Dollars = 'Dollar'
Yens = 'Yen'
Euros = 'Euros'
#This sets the variable names for the currency's (Lines 3 to 6)
rates = [1, 2, 3, 4]
#This makes a variable called 'rates' and has the currency exchange rates stored in the variable
print ("Welcome to the Currency Converter")
#Welcomes the user to the converter and asks for the user to enter their name
def ask(direction):
    print ("Pound", rates[0])
    print ("Dollars", rates[1])
    print ("Euro", rates[2])
    print ("Yen", rates[3])
    choice = int(input("Please enter your choice: "))
    return (choice)

convertrates1 = 1
convertrates2 = 1.6
convertrates3 = 1.2
convertrates4 = 200

cfrom=ask("From")-1
cto=ask("to")-1

entry=float(input("You have selected {0}. Now please enter a sum of money to convert: ".format(currencies[cfrom])))
answer= (entry/rates[cfrom])*rates[cto]
print ("{0:.2f})".format(answer))

# if choice == rates[0]:
#     print ("You have selected Pounds")
#     answer = (entry*convertrates1[0])
#     print(answer)

# if choice == rates[1]:
#     print ("You have selected Dollars")
#     answer = (entry*convertrates2[1])

# if choice == rates[2]:
#     print ("You have selected Euros")
#     answer = (entry*convertrates3[2])

# if choice == rates[3]:
#     print ("You have selected Yen")
#     answer = (entry*convertrates4[3])



converting = input("Please enter the sum you wish to convert in the currency you chose: ")


