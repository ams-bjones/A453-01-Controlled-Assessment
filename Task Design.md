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
Task 2
====
Creating an Address Book
#What I need to include:
a) A surname and first name
b) Two lines of the address and a post code
c) Telephone number
d) Date of Birth
e) E-Mail address
Create a programme to search a data file by:
a) A surname to retrieve and show details if correct
b) By date of birth to retrieve and all contacts with a birthday in that month
