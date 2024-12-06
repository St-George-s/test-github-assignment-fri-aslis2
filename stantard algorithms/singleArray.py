
def find_max(times_spent):
    max_value = times_spent[0] 
    for counter in range(1, len(times_spent)):
        if times_spent[counter] > max_value:
            max_value = times_spent[counter]
            print("The maximum time spent was " + str(max_value))

    #for time in times_spent:
        #if time > max_value:
           # max_value = time
           # print("The maximum time spent was " + str(max_value))


def find_min(times_spent):
    min_value = times_spent[0]
    for counter in range(len(times_spent)):
        if times_spent[counter] < min_value:
            min_value = times_spent[counter]
            print("The minimum time spent was " + str(min_value))


def linear_search(times_spent,search_time):
    found = False 
    counter = 0 
    array_size = len(times_spent)
    while counter < array_size and not found:
        if times_spent[counter]==search_time:
            found = True 
        else:
            counter +=1
            
    if found:
        print(str(search_time) + " found at position " + str(counter))
    else:
        print("Not found")

def count_occurrences(times_spent, search_time):
    found = 0 
    for time in times_spent:
        if time == search_time:
            found += 1 
            print(" Time " + str(search_time) + " hours appeared " + str(found) + " times in the array")



times_spent = [5, 3, 4, 6, 5]
find_max(times_spent)
find_min(times_spent)
linear_search(times_spent, 4)
count_occurrences(times_spent, 5)