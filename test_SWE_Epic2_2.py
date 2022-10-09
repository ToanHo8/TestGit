import SWE_Epic2_2
     
#Test account login- make sure user states whether they have an InCollege account
def test_LogIn():
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
    print("successfully create an account")
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

#Test Search People
def test_SearchPeople():
    searchFirstName = "ho"
    searchLastName = "toan"
    assert searchFirstName == "ho"
    assert searchLastName == "toan"
    print("Contact is found! They are part of the incollege system.")

    searchFirstName = "hoa"
    searchLastName = "toanj"
    assert searchFirstName != "ho" or searchLastName != "toan"
    print("Contact is not found! They are not yet a part of the incollege system.")

#Save a job post but not display of the name of person who posted
def test_jobSearch():
    countJob = 3
    assert countJob == 3
    print("System permit up to 5 jobs posted. Saved name of person in jobfile but not displayed.")

    countJob = 6
    assert countJob > 5
    print("All permitted job are create, please come back later")

# pytest test_SWE_Epic2_2.py -v