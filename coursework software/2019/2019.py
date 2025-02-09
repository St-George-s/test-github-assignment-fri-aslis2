import csv 

class Members:
    def __init__(self, forename, surname,distance):
        self.forename = forename
        self.surname = surname 
        self.distance = distance 

# Comment
def read_data():
    file ="coursework software/2019/members.txt"
    with open(file,'r') as file:
        reader = csv.reader(file)
        members = []
        # Crete a record for each row
        for row in reader :
            newRecord = Members (row[0], row[1], float(row[2]))
            members.append(newRecord)

    return members

# Comment
def find_max(members):
    max_value = members[0].distance
    for member in members[1:]:
        if member.distance > max_value:
           max_value = member.distance
    return max_value

# Coment
def print_max(max_value):     
    print("The furthest distance walked is  " + str(max_value))


# Coment
def prizeWinners(members, max_value):
    with open('results.txt', 'w', newline= '' ) as file:
        file.write("The prize winning members are:" + "\n")
        for member in members:
            # Comment
            if member.distance > 0.7 * max_value:
                file.write( member.forename  + member.surname +"\n")
        file.write("The number of whole marathons walked by each member is:" + "\n" )
        for member in members:
            # Coment
            if member.distance/26.22 > 1 :
                marathon =int(member.distance/26.22)
                file.write( member.forename + ","  + member.surname + "," + str(marathon)+ "\n")

# Main Program
members = read_data()
max_value = find_max(members)
print_max(max_value)
prizeWinners(members, max_value)

