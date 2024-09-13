def get_destination():
    print("")
    destination = input("Enter the travel destination (type END to stop): ")
    return destination

def get_number_of_people():
    people_count = input("Enter the number of people: ")
    return people_count

def get_travel_method():
    travel_method = input("Enter travel method: ")
    return travel_method

def print_travel_details(destination, people_count, travel_method):
    print(destination, people_count, travel_method)

def print_all_trips(destinations, people_counts, travel_methods):
     print(destinations, people_counts, travel_methods)
    


#main
destinations = []
people_counts = [] 
travel_methods = [] 
local_destinations = ["Edinburgh", "Glasgow", "Dundee", "Aberdeen"]

destination = get_destination()
destinations.append(destination)

while destination.upper() != "END":
    people_counts.append(get_number_of_people())

    if destination in local_destinations:
        travel_method = "Local transport"
    else:
        travel_methods.append(get_travel_method())

    print_travel_details(destination, people_counts, travel_method)
    destination = get_destination()
    destinations.append(destination)



# destination.append(people_count)
# travel_method.append(travel_method)
# summarise_trips(destination, people_count, travel_method)
# search_destination = input("Enter a destination to search")
# find_by_dest(destination, people_count, travel_method)







