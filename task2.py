# surnames = {
#     "Jackson": ["Samantha Jackson", "2 Heather Row", "Basingstoke", "RG21 3SD", "01256 135434",	"23/04/1973", "sam.jackson@hotmail.com"]
#     "VickersJ": ["Jonathan",	"18 Saville Gardens", "Reading", "RG3 5FH",	"01196 678254",	"04/02/1965", "the_man@btinternet.com"]
#     "Morris": ["Sally", "The Old Lodge", "Hook", "RG23 5RD", "01256 728443", "19/02/1975", "smorris@fgh.co.uk"]
#     "Cobbly": ["Harry", "345 The High Street", "Guildford", "GU2 4KJ", "01458 288763", "30/03/1960", "harry.cobbly@somewhere.org.uk"]
#     "Khan": ["Jasmine", "36 Hever Avenue", "Edenbridge", "TN34 4FG", "01569 276524", "28/02/1980", "jas.khan@hotmail.com"]
#     "VickersH": ["Harriet", "45 Sage Gardens", "Brighton", "BN3 2FG", "01675 662554", "04/04/1968", "harriet.vickers@btinternet.com"]
#     }

addresses = []
def getAddrs():
    with open('addressbook.csv')as book:
        data = book.read()
        for line in data.split('\r\n'):
            address= line.split(',')
            addresses.append(address)
            
getAddrs()


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
    

def evaluate_choice(choice):
    if choice == "1":
        surname_search = raw_input("\nWhat Surname do you wish to search for?: ")
        for address in addresses:
            if surname_search == address[0]:
                print address
    
    elif choice == "2":
        month_search = raw_input("\nWhat Birthday month do you wish to search for? (Please enter in 2-digit format e.g Feb = 02): ")
        for address in addresses:
            if len(address)>6:
                dd,mm,yy = address[6].split('/')
                if month_search == mm:
                    print address

    else:
        print "\nThat is not a valid choice, please restart the programme and try again."
    
evaluate_choice(choice)
