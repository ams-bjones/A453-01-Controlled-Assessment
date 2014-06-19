###Reference: http://stackoverflow.com/questions/20398017/showing-decimal-places-python-2-7-and-decimal-datatype###
#setup the decimal data type (including number of decimal places)
import decimal

print("Welcome to the Currency converter!")
#Welcomes the user to the currency converter
currencyAmount = decimal.Decimal(raw_input('Please enter the value of which you wish to convert: '))

#Asks the user to enter the value that they wish to convert. The value is stored in the variable "currencyAmount
currencyType = int(raw_input('Please enter the currency type for the value you entered (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))
currencyType = int(raw_input('please enter the type (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))
#asks for the current value and type from the user

#set the exchange rates (based on the GBP)
euro = decimal.Decimal('1.2')
#Sets the variable "euro" to 1.2 times the GBP rate. This figure can be easily changed by the user without having to change anything else.
dollar = decimal.Decimal('1.6')
#Sets the variable "dollar" to 1.6 times the GBP rate. This figure can be easily changed by the user without having to change anything else.
yen = decimal.Decimal('200')
#Sets the variable "yen" to 200 times the GBP rate. This figure can be easily changed by the user without having to change anything else.

#Converts the currency into pound sterling
dollar = decimal.Decimal('1.6')
yen = decimal.Decimal('200')

#convert the currency into pound sterling
if (currencyType == 2):
    currencyAmount = currencyAmount / euro
elif (currencyType == 3):
    currencyAmount = currencyAmount / dollar
elif (currencyType == 4):
    currencyAmount = currencyAmount / yen

#ask the user what currency they want it converted into
currencyConvert = int(raw_input('Please enter the currency you wish to convert to (1 = pound, 2 = euro, 3 = dollar, 4 = yen): '))

#convert the currency into the new format (GBP already done in previous steps)
#convert the currency into the new format (pound already done in previous steps)
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

print 'The result of the Currency Conversion was ',  currencyAmount
print ("Thank you for using the Currency Converter!")
