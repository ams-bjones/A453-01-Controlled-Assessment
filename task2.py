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