import csv 
 
#Get new member data
get_firstname = input("Enter first name")
get_surname = input("Enter surname")
get_category = input("Enter category")

#Validate password 
def validPassword():
    #Loop until password is valid
    while True:
        get_password = input("Please enter password")
        #Convert first character to ASCII value 
        firstChar = ord(get_password[0])
        #Convert last character to ASCII value 
        lastChar = ord(get_password[-1])
        #Check that the first character is a capital letter and that the last character is #, $ or % 
        if 65 <= firstChar <= 90 and 35<= lastChar <= 37:
            print("Valid password")
            break
            return password
        else:
            print("Invalid password, Please try again")

firstname = []
surname = []
category = []
password = []

#Read member data from file into parallel arrays 
def read_update_data():
    with open("coursework software/2020/members.txt", 'r' ) as file:
        reader = csv.reader(file)
        for row in reader:
            firstname.append(row[0])
            surname.append(row[1])
            category.append(row[2])
            password.append(row[3])


    get_password = validPassword()
    
    #Add new member data into existing parallel arrays 
    firstname.append(get_firstname)
    surname.append(get_surname)
    category.append(get_category)
    password.append(get_password)

    #Display the first name, surname and category of all members
    print("\nOur members are :")
    for i in range(len(firstname)):
        print(f"{firstname[i]} {surname[i]} {category[i]}")
    return firstname, surname, category, password
 
def count_occurrences(category):
    #Count number of Adult members
    category_adult = ("Adult")
    count = 0
    for cat in category:
        if cat == category_adult:
            count += 1 
    print("There are currently " + str(count) + " Adult members")

    #Count number of Junior members 
    category_junior = ("Junior")
    found = 0 
    for cat in category:
        if cat == category_junior:
            found += 1 
    print("There are currently " + str(found) + " Junior members")

    #Count number of Senior members 
    category_senior = ("Senior")
    counter = 0
    for cat in category:
        if cat == category_senior:
            counter += 1 
    print("There are currently " + str(counter) + " Senior members")
    
    #Count total memberships 
    total_members = 0
    for cat in category:
        if cat == cat:
            total_members += 1 
    print("Total current membership is " + str(total_members))

#main
validPassword()
read_update_data()
count_occurrences(category)