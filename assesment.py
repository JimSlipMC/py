import random
login = True

def options():
    datafile = open("data.txt",  "a+")
    print("Please select an option from below!")
    print("1) Add a usser to the system 2) Get all students in the  system.")
    option = input("> ")

    if option == "1":
        print("Please enter all details required into the system!")
        print("")
        forname = input(" > Enter students forname: ")
        sirname = input(" > Enter students sirname: ")
        gender = input(" > Enter students gender: ")
        dob = input(" > Enter students Date Of Birth (format 00/00/0000)")

        userid = forname[0] + sirname + "-" + str(random.randint(0,1000))

        datafile.write("--------------------------\n")
        datafile.write("Forname: " + forname + "\n")
        datafile.write("Sirname: " + sirname + "\n")
        datafile.write("Gender: " + gender + "\n")
        datafile.write("DOB: " + dob + "\n")
        datafile.write("UUID: " + userid + "\n")
        datafile.close()
        options()

    elif option == "2":
        datafile = open("data.txt", "a+")
        read = datafile.read()
        print(read)
        
        

while login:
    print("")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    print("")

    if username == "m" and password == "p":
        login = False
        options()
    elif username == "m" and password != "p":
        print("invalid password, if this is an error please contact IT support @ itsupport@treeroadschool.co.uk")

    elif username != "m" and password == "p":
        print("Invalid username, if this is an error please contact IT support @ itsupport@treeroadschool.co.uk")

    else:
        print("Login credentials incorrect, if this is an error please contact IT support @ itsupport@treeroadschool.co.uk")
