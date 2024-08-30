def get_destination():
    destination = input("Enter the travel destination (type END to stop): ")
    return destination

def get_number_of_people():
    people_count = input("Enter the number of people")
    return people_count

def get_travel_method():
    travel_method = input("Enter travel method")
    return travel_method

def print_travel_details(destination, people_count, travel_method):
    print(destination, people_count, travel_method)

#main
destination = get_destination()
people_count = get_number_of_people()
travel_method = get_travel_method()
print_travel_details(destination, people_count, travel_method)


