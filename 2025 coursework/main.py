import csv 

class Orders:
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating

#Read from file into array of records 
def readData():
    file ="2025 coursework/orders.txt"
    with open(file,'r') as file:
        reader = csv.reader(file)
        orders = []
        # Create a record for each row
        for row in reader :
            newRecord = Orders (row[0], row[1],row[2],row[3], row[4], row[5])
            orders.append(newRecord)

    return orders


#Find the position of the customer who gave the first 5-star rating in a given month.
def findPosition(orders):
    position = -1
    index = 0 
    #Ask user to enter month to search for
    month = input("Enter month ")
    while position == -1 and index < len(orders):
        #Use string manipulation to get the portion of the string thats the month and check if the rating is 5
        if month == (orders[index].date[3:6]) and str(orders[index].rating) == "5":
            position = index
        index = index + 1 
    return position


#Write details of the winning customer, or ‘no winner’ message, to a text file.
def winningCustomers(orders, position):
    with open('winningCustomer.txt', 'w', newline= '' ) as file:
        if position >= 0:
                file.write(orders[position].orderNum + "," + orders[position].email + "," + orders[position].cost + "\n" )
        else:
            file.write("No winner" + "\n")


#Display the total number of orders delivered and the total number of orders collected.       
def countOption(orders):
    count = 0
    for i in range(0, len(orders)):
        if "Delivery" == orders[i].option :
            count = count +1 
    print("Total number of orders delivered to date: " + str(count))

    found = 0
    for i in range(0, len(orders)):
        if "Collection" == orders[i].option :
            found = found +1 
    print("Total number of orders collected to date: " + str(found))



#main
orders = readData() 
position = findPosition(orders)
winningCustomers(orders, position)
countOption(orders)



