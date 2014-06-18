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