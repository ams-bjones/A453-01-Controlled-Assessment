Creating a Currency Converter. (Task 1)
====

That...

a) Has exchange rates that can be regularly changed by the user.

b) User should be able to enter an amount, select chosen currency, and the currency to convert it into.

c) Figure shown should be to two decimal places.

Currencys required: GBP (£) Euro (€) USD ($) and JPY (¥)

Tests
====

Import symbols        (GBP, EUR, USD, JPY)
import exchange rates   (1, 1.2, 1.6, 200)

GBP -> EUR = 1/GBP * EUR

GBP -> USD = 1/GBP * USD

GBP -> JPY = 1/GBP * JPY

EUR -> GBP = 1/EUR * EUR

EUR -> USD = 1/EUR * USD

EUR -> JPY = 1/EUR * JPY

Pseudocode
==========
```
Variable = Currencys
Import Rates (Variablename)

print Ask user what currency they are converting from

If choice is Pounds
  convert to dollar/ euro/ yen (user choice)
If choice is Dollar
  convert to Pounds/ euro/ yen (user choice)
If choice is Euro
  convert to Pounds/ dollar/ yen (user choice)
If choice is Yen
  convert to Pounds/ dollar/ euro (user choice)

print conversion
  else print error
```
Attempt 1
====
```python
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

 if choice == rates[0]:
     print ("You have selected Pounds")
     answer = (entry*convertrates1[0])
     print(answer)

 if choice == rates[1]:
     print ("You have selected Dollars")
     answer = (entry*convertrates2[1])

 if choice == rates[2]:
     print ("You have selected Euros")
     answer = (entry*convertrates3[2])

 if choice == rates[3]:
     print ("You have selected Yen")
     answer = (entry*convertrates4[3])



converting = input("Please enter the sum you wish to convert in the currency you chose: ")
```
Attempt 2 (Successful)
====
```python
###Reference: http://stackoverflow.com/questions/20398017/showing-decimal-places-python-2-7-and-decimal-datatype###
#setup the decimal data type (including number of decimal places)
import decimal

print("Welcome to the Currency converter!")
#Welcomes the user to the currency converter
currencyAmount = decimal.Decimal(raw_input('Please enter the value of which you wish to convert: '))
#Asks the user to enter the value that they wish to convert. The value is stored in the variable "currencyAmount
currencyType = int(raw_input('Please enter the currency type for the value you entered (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))
#asks for the current value and type from the user

#set the exchange rates (based on the GBP)
euro = decimal.Decimal('1.2')
#Sets the variable "euro" to 1.2 times the GBP rate. This figure can be easily changed by the user without having to change anything else.
dollar = decimal.Decimal('1.6')
#Sets the variable "dollar" to 1.6 times the GBP rate. This figure can be easily changed by the user without having to change anything else.
yen = decimal.Decimal('200')
#Sets the variable "yen" to 200 times the GBP rate. This figure can be easily changed by the user without having to change anything else.

#Converts the currency into pound sterling
if (currencyType == 2):
    currencyAmount = currencyAmount / euro
elif (currencyType == 3):
    currencyAmount = currencyAmount / dollar
elif (currencyType == 4):
    currencyAmount = currencyAmount / yen

#ask the user what currency they want it converted into
currencyConvert = int(raw_input('Please enter the currency you wish to convert to (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))

#convert the currency into the new format (GBP already done in previous steps)
if (currencyConvert == 2):
    currencyAmount = currencyAmount * euro
elif (currencyConvert == 3):
    currencyAmount = currencyAmount * dollar
elif (currencyConvert == 4):
    currencyAmount = currencyAmount * yen

#displays the end result to the user
print 'The result of the Conversion was: ',  currencyAmount
#Thanks the user for using the Currency Converter
print ("Thank you for using the Currency Converter!")
```

Creating an Address Book (Task 2)
====
#What I need to include:
a) A surname and first name
b) Two lines of the address and a post code
c) Telephone number
d) Date of Birth
e) E-Mail address
Create a programme to search a data file by:
--------------------------------------------
a) A surname to retrieve and show details if correct
b) By date of birth to retrieve and all contacts with a birthday in that month

Pseudocode
====
Load preset address book
create function to add details
create function to search for details in a preset file
searchable by surname
searchable by month of birth


Successful Attempt #1 
====
```python
#The address' provided
# surnames = {
#     "Jackson": ["Samantha Jackson", "2 Heather Row", "Basingstoke", "RG21 3SD", "01256 135434",	"23/04/1973", "sam.jackson@hotmail.com"]
#     "VickersJ": ["Jonathan",	"18 Saville Gardens", "Reading", "RG3 5FH",	"01196 678254",	"04/02/1965", "the_man@btinternet.com"]
#     "Morris": ["Sally", "The Old Lodge", "Hook", "RG23 5RD", "01256 728443", "19/02/1975", "smorris@fgh.co.uk"]
#     "Cobbly": ["Harry", "345 The High Street", "Guildford", "GU2 4KJ", "01458 288763", "30/03/1960", "harry.cobbly@somewhere.org.uk"]
#     "Khan": ["Jasmine", "36 Hever Avenue", "Edenbridge", "TN34 4FG", "01569 276524", "28/02/1980", "jas.khan@hotmail.com"]
#     "VickersH": ["Harriet", "45 Sage Gardens", "Brighton", "BN3 2FG", "01675 662554", "04/04/1968", "harriet.vickers@btinternet.com"]
#     }

#Loads up the address file found in the file named 'addressbook.csv'
addresses = []
def getAddrs():
    with open('addressbook.csv')as book:
        data = book.read()
        for line in data.split('\r\n'):
            address= line.split(',')
            addresses.append(address)
#Calls the function 'getAddrs'
getAddrs()

#Welcomes you to the Address Book
print("Welcome to the Address Book!")
answer = raw_input("Are you creating an entry? (Press 1) \nOr, are you searching an entry? (Press 2) ")

#If creating a file
if answer == "1" : 
    print (" You have selected to create an entry.")
    # collects information

    lastname = raw_input("What is the persons last name? ")
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What is the persons phone number? ")
    email = raw_input("What is the persons email address? ")
    address = raw_input("What is the persons address? ")

    #create or append addressbook.csv

    tempfile = open("addressbook.csv","a")
    
    #create string to print to file
    #print tempfile
    #print (firstname + " " + lastname + ", " + phone + ", " + email + ", " + address) 

    tempfile.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
    tempfile.write("\n")
    
    
    
#If searching for a file already created

elif answer == '2':
    choice = raw_input("You have selected to search for an entry. Would you like to search by surnames [Press 1] \n Or by month of birth [Press 2]")
    
#if the user selects '1', the system asks what surname they are searching for
def evaluate_choice(choice):
    if choice == "1":
        surname_search = raw_input("\nWhat Surname do you wish to search for?: ")
        for address in addresses:
            if surname_search == address[0]:
                print address
#The above code deciphers the people from the list in the address book who have the surname selected
#If the user selects '2', the system asks what birthday month they are searching for
    elif choice == "2":
        month_search = raw_input("\nWhat Birthday month do you wish to search for? (Please enter in 2-digit format e.g Feb = 02): ")
        for address in addresses:
            if len(address)>6:
                dd,mm,yy = address[6].split('/')
                if month_search == mm:
                    print address
#The above code deciphers the people from the list in the address book of who is in the month selected

    else:
        print "\nThat is not a valid choice, please restart the programme and try again."
#If the user says anything other than '1' or '2', then the system prints that it isnt a valid choice and asks for the user to reselect their option by rerunning the programme.
```python

Finding ISBN's of books (Task 3)
====
#What i need to include
Create a programme to take a 10 digit number and calculate the correct 11 didgit ISBN.
It should:
A) only contain the digits 1-9
B) only accept a number of the correct length

Pseudocode
====
Take the 10 digit book number
Mult by 10-2, down one by each number
take answer
then
add result of all numbers
divide by 11
subtract remainder from 11
print answer

Succesful Attempt
====
```python
#Reference: http://stackoverflow.com/questions/21814563/need-python-help-for-isbn-calculator

#Creates a large string (seen by the the triple '"', means you can have several lines of text in one string
decision = str(input(""" What would you like to do?; 
1) Convert a 10 digit number to an ISBN number  
2) Rage Quit and end the programme""")) 

#Defines 'rage_quit' to quit upon being entered. See line 14 for an example.
def rage_quit():
    quit()

#If the user chooses 2 at the title screen, the programme prints that you have rage quit, and ends the programme.    
if decision == "2": 
    print ("\nYou have successfully Rage Quit. Congratulations!!!")
    rage_quit()

#elif = Else and if. So if the user selects '1', the programme asks the user to enter a 10 digit number.
elif decision == "1": 
    ISBN=raw_input("Enter a 10 digit number: ") 

#While the length of the input ISBN is not equal to 10, print please enter a 10 digit number.
while len(ISBN)!= 10: 

    print('YOU DID NOT ENTER A 10 DIGIT NUMBER !!!') 
    ISBN=int(input('Please enter a 10 digit number: ')) 
    continue

#If the input of the ISBN is equal to a length of 10, multiply the first number in the variable ISBN by 11. Etc.
else: 

    Di1=int(ISBN[0])*11
    Di2=int(ISBN[1])*10
    Di3=int(ISBN[2])*9
    Di4=int(ISBN[3])*8
    Di5=int(ISBN[4])*7
    Di6=int(ISBN[5])*6
    Di7=int(ISBN[6])*5
    Di8=int(ISBN[7])*4
    Di9=int(ISBN[8])*3
    Di10=int(ISBN[9])*2

#The sum of digits 1-10
sum=(Di1+Di2+Di3+Di4+Di5+Di6+Di7+Di8+Di9+Di10) 

#the variable 'num' is set to the remainder of the variable 'num'
num=sum%11
#Digit 11 is set to 11 subtracted by the variable 'num'
Di11=11-num 
#If digit 11 is equal to 10, set the variable 'di11' to 'x'
if Di11==10: 
    Di11='X'
#The ISBN is equal to the string ISBN + the string of Di11
ISBNNumber=str(ISBN)+str(Di11)
#Prints the ISBN number from the formula in line 53
print('The ISBN number is -->    ' + ISBNNumber) 
```python
