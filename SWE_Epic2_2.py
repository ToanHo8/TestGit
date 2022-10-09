#Epic 2

#Global Variables
user = ""


#AFTER LOGIN = HOME PAGE
#created a function in order to call it again when asked to return to the main screen
def additionalOptions():
    global user
    addiOption = str(input("\nPress J to search for a job:\n"
                        "Press F to find someone you know:\n"
                        "Press S to learn a new skill:\n"))
    if addiOption == "J" or addiOption == "j":
        jobSearch(user)

    if addiOption == "F" or addiOption == "f":
        SearchPeople()

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


def jobSearch(user):
    #Ask user if they want to add a job or return
    NewJobPost =str(input("\nPost a job or return? (y/n/r)\n"))
    while True: #Keep going until a valid option is put
        if NewJobPost == "Y" or NewJobPost == "y":
            jobTitle = input("Job title:\n")
            description = input("Description:\n")
            employer = input("Employer:\n")
            location = input("Location\n")
            salary = input("Salary:\n")

            file = open("jobfile.txt", "a")
            file.write(user)
            file.write(" ")
            file.write(jobTitle)
            file.write(" ")
            file.write(description)
            file.write(" ")
            file.write(employer)
            file.write(" ")
            file.write(location)
            file.write(" ")
            file.write(salary)
            file.write("\n")
            

            countJob = 0
            with open(r"jobfile.txt", 'r') as file:  #read each job line save in txt
                countJob = len(file.readlines())
                #print(countAcc)

            if countJob > 5:
                print ("All permitted jobs are created, please come back later")
            file.close
            break
        elif NewJobPost == "R" or NewJobPost == "r":
            additionalOptions()
        elif NewJobPost == "N" or NewJobPost == "n":
            break
        else:  
            NewJobPost =str(input("Invalid option, please try again. (y/n/r)"))

    
def SearchPeople():
    userFound = False
    searchFirstName = str(input("\nEnter the first name of the person who you would like to find, or enter R to return\n"))
    if searchFirstName == "R" or searchFirstName == "r":
        return 0
    searchLastName = str(input("\nEnter the last name of the person you would like to find\n"))
    for line in open("userfile.txt", "r").readlines():
        savedLogin = line.split() #stores results in a list of two strings and splits on the space
        if searchFirstName.lower()==savedLogin[2].lower() and searchLastName.lower()==savedLogin[3].lower():
            userFound = True
            print("They are Part of the InCollege System.")
            break

    if userFound == False:
        print("They are not yet a part of the InCollege system.")

    return userFound

#Pre-login screen
def loginOptions():
    LogOption =str(input("\nDo you have an InCollege account?\n"
                     "Press Y to login or N to create a new account: \n"
                     "Press F to find contacts in InCollege: "))
    while True:
        if LogOption == "Y" or LogOption == "y" or LogOption == "L" or LogOption == "l":
            LogIn()
            break
        if LogOption == "N" or LogOption == "n" or LogOption == "Y" or LogOption == "s":
            CreateAcc()
            break
        if LogOption == "F" or LogOption ==  "f":
            if SearchPeople():
                LogOption = str(input("\nLog in (L) or sign up (S) to join your friends\n"))
            #loginOptions() #after showing people in contacts, display login options again
         
        else:
            LogOption =str(input("\nDo you have an InCollege account?\n"
                        "Press Y to login or N to create a new account: "))

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
            #after username and password are valid, ask for first and last name, and store new user password, first name, and last name in file          
            firstName = str(input("\nPlease enter your first name \n"))
            lastName = str(input("\nPlease enter your last name\n"))

            file = open("userfile.txt", "a")
            file.write(newUser)
            file.write(" ")
            file.write(newPass)
            file.write(" ")
            file.write(firstName)
            file.write(" ")
            file.write(lastName)
            file.write("\n")

            countAcc = 0
            with open(r"userfile.txt", 'r') as file:  #read each account line save in txt
                countAcc = len(file.readlines())
                #print(countAcc)

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
    global user
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
        break #break out of while loop

def WatchVideo():
    print("Video is now playing...")


#THIS is MAIN FUNC
def main():
    #Using existing InCollege account or Creating a new account
    UserStory = print("Welcome to InCollege! InCollege is a website to help college students make connections and get jobs. Don't believe us? Take it from our users! \n\"I was a senior about to graduate without a job, but with the help of InCollege, I got a job and am now a very successful person\" -John Doe")
    VideoOption = str(input("Want to see more on how InCollege has brightened the future of college students? Watch this video! (Y/N)"))
    if VideoOption == "Y" or VideoOption == "y":
        WatchVideo()

    #call prelogin screen
    loginOptions()
  
if __name__ == "__main__":
    main()
#END OF MAIN FUNC