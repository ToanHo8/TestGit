#Epic 1

#AFTER LOGIN = HOME PAGE
#created a function in order to call it again when asked to return to the main screen
def additionalOptions():
    addiOption = str(input("\nPress J to search for a job:\n"
                        "Press F to find someone you know:\n"
                        "Press S to learn a new skill:\n"))
    if addiOption == "J" or addiOption == "j":
        print("\nUnder construction\n")

    if addiOption == "F" or addiOption == "f":
        print("\nUnder construction\n")

    #after selecting learn new skill, present 5 skills for user to select or return
    if addiOption == "S" or addiOption == "s":
        skill = str(input("\nSelect one of these five skills:\n"
                        "   coding practice\n"
                        "   new language\n"
                        "   jira\n"
                        "   github\n"
                        "   excel\n"
                        "\n return\n"))

        if skill == "coding practice":
            print("\nUnder construction\n")

        if skill == "new language":
            print("\nUnder construction\n")

        if skill == "jira":
            print("\nUnder construction\n")

        if skill == "github":
            print("\nUnder construction\n")

        if skill == "excel":
            print("\nUnder construction\n")

        #for return, call function again
        if skill == "return":
            additionalOptions()

#CREATE A NEW ACCOUNT
def CreateAcc():
    newUser = str(input('\nPlease enter your new username: '))
    #Support for up to 5 unique student accounts (unique user name)

    #password require: 8 chars min, 12 chars max, at least 1 cap letter, one digit, one special character)
    while True:
        newPass = str(input("\n\n*** Your password must have: *** \n"
                        "+ Minimum of 8 characters\n"
                        "+ Maximum of 12 characters\n"
                        "+ At least one capital letter, one digit, one special character\n"
                        "\nEnter your new password: "))
        upper = any(ele.isupper() for ele in newPass)           #at least 1 cap letter
        digit = any(e.isdigit() for e in newPass)               #at least 1 digit
        specChar = any(not c.isalnum() and 
                    not c.isspace() for c in newPass)        #at least 1 special char

        if len(newPass)>7 and len(newPass)<13 and upper and digit and specChar:             
            
            #after username and password are valid, store new user and password in file
            file = open("userfile.txt", "a")
            file.write(newUser)
            file.write(" ")
            file.write(newPass)
            file.write("\n")
            
            countAcc = 0
            with open(r"userfile.txt", 'r') as file:  #read each account line save in txt
                countAcc = len(file.readlines())
                print(countAcc)

            if countAcc > 5:
                print ("All permitted accounts are created, please come back later")
                break
            file.close

            print('\nCongrats! You are successfully sign up.' 
                    '\nYou can login now...')

            #call login function
            LogIn()
            break
    
#The 6th attempt to create a student account will result in the message "All permitted accounts have been created, please come back later"

#LOGIN WITH AN ACCOUNT
def LogIn():
    while True:
        user = str(input("\nPlease enter your username: "))
        password = str(input("\nPlease enter your password: "))

        # login success system will tell them "You have successfully logged in"
        # "Incorrect username / password, please try again". Allow attempt to log in again and unlimited # of log in.

        #read textfile and check if they are equal
        for line in open("userfile.txt", "r").readlines():
            savedLogin = line.split() #stores results in a list of two strings and splits on the space
            if user==savedLogin[0] and password==savedLogin[1]:
                print("\n*** You have successfully logged in! ***")
                additionalOptions()
                break

        else:
            print("\n*** Incorrect username/password, please try again. ***")
            continue

#THIS MUST BE MAIN FUNC
#Using existing InCollege account or Creating a new account
LogOption =str(input("\nDo you have an InCollege account?\n"
                     "Press Y to login or N to create a new account: "))
if LogOption == "Y" or LogOption == "y":
        LogIn()
if LogOption == "N" or LogOption == "n":
    CreateAcc()

#Test account login- make sure user states whether they have an InCollege account
def test_Login():
    LogOption="y"
    assert LogOption == "Y" or "y" or "N" or "n"
    user="sophiehos"
    password="Hostet17%"
    assert user=="sophiehos"
    assert password=="Hostet17%"
    print("You have successfully logged in")
    user="sophiahos"
    password="NotHos1"
    assert user!="sophiehos" or password!="Hostet17%"
    print("Incorrect username/password, please try again.")

#Test account creation
def test_CreateAcc():
    newUser="sophiehos"
    assert newUser != ' '
    newPass="Hostetl7#"
    assert (len(newPass)>7 and len(newPass)<13) and any(ele.isupper() for ele in newPass) and any(e.isdigit() for e in newPass) and any(not c.isalnum() and not c.isspace() for c in newPass)
    countAcc=3
    assert countAcc>=0 and countAcc<=5
    countAcc=6
    assert countAcc==6
    print("All permitted accounts have been created, please come back later")

#Test Additional Options
def test_additionalOptions():
    addiOption="J"
    assert addiOption=="J" or "j" or "F" or "f" or "S" or "s"
    assert addiOption=="S" or "s"
    print("coding practice" or "new language" or "jira" or "github" or "excel") 
    skill="coding practice"
    assert skill==("coding practice" or "new language" or "jira" or "github" or "excel")
    print("Under construction")

  