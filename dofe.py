import random 

def username_generation(firstName,lastName):
    username = firstName[0:3] + lastName[0:3]
    myNum = str(random.randint(100,999))
    username = username + myNum 
    return username



firstName = input("Enter your first name")
lastName = input("Enter your last name")
awardLevel = input("Enter your DofE award level")

username = username_generation(firstName,lastName)
print(username)