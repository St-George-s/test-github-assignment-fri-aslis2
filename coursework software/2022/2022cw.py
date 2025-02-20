import csv 

class Sightings:
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date 
        self.age = age 

def upppercase(word):
    # Get ASCII value of first character
    firstChar = ord(word[0])
    if firstChar >= 97 and firstChar <=122:
        firstChar = firstChar - 32 
        word = (chr(firstChar) + word[1:])
    return word 


def read_data():
    file ="coursework software/2022/mammals.txt"
    with open(file,'r') as file:
        reader = csv.reader(file)
        # next(reader)
        sightings = []
        for row in reader :
            newRecord = Sightings(row[0], row[1], (row[2]), int(row[3]))
            sightings.append(newRecord)

    return sightings 


def find_max(sightings):
    max_value = sightings[0]
    for sighting in sightings[1:]:
        if sighting.age > max_value.age:
           max_value = sighting
        
    print("The oldest walker is " + str(max_value.age) + " years old")


def find_sightings_by_mammal(sightings):
    town = input("Enter town: ")
    town = upppercase(town)
    mammal = input("Enter mammal: ")
    mammal = upppercase(mammal)
    # Same here for mammal
    print("The dates of sightings were:")
    for sighting in sightings:
        if sighting.town == town and sighting.mammal == mammal:
            print(sighting.date)

# Sort code here o match pseudocode
def count_sightings_per_date(sightings):
    dayToCount = sightings[0].date
    count = 1

    for sighting in sightings[1:]:
        if dayToCount == sighting[0].date:
            count = count + 1 
        else:
            print(dayToCount + count)
            dayToCount = sighting[0].date
            count = 1 
        print("On " , dayToCount, "there were ", count,"sightings.")



#main
sightings = read_data()
find_max(sightings)
find_sightings_by_mammal(sightings)
count_sightings_per_date(sightings)
        

count = 0
    delivered = "Delivery"
    for order in orders[0:]:
        if delivered == orders[0].option  :
            count = count + 1 
        else:
            count = count
    print("Total number of orders delivered to date: " + str(count))


 with open('winningCustomer.txt', 'w', newline= '' ) as file:
        for order in orders:
            if position >= 0:
                file.write(orders.orderNum + "," + orders.email + "," + orders.cost + "\n" )
            else:
                file.write("No winner" + "\n")