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
def read_data():
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
def find_Position(orders):
    position = -1
    index = 0 
    month = input("Enter month ")
    while position == -1 and index < len(orders):
        if month == (orders[index].date[3:6]) and orders[index].rating == 5:
            index = position
        index = index + 1 
        break
    print(orders[index].rating)
    print(orders[index].date[3:6])
    print(position)
    return position


def winningCustomers(orders, position):
    with open('winningCustomer.txt', 'w', newline= '' ) as file:
        if position >= 0:
                file.write(orders.orderNum + "," + orders.email + "," + orders.cost + "\n" )
        else:
            file.write("No winner" + "\n")
        
def totalOrders_Delivered_Collected(orders):
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
orders = read_data() 
position = find_Position(orders)
winningCustomers(orders, position)
totalOrders_Delivered_Collected(orders)



