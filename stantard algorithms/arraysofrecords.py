
class Student:
    def _init_(StudentNames, Activities, times_spent):
        self.StudentNames = StudentNames
        self.Activities = Activities
        self.times_spent = times_spent

def record_storing():
    for i in range(0, len(times_spent)):
        student_activities = [Student(StudentNames[i], Activities[i], times_spent[i])]
    return student_activities

def find_max(times_spent):
 max_value = times_spent[0]
 for time in times_spent:
        if time > max_value:
           max_value = time
           print("The maximum time spent was " + str(max_value))


def find_min(times_spent):
 min_value = times_spent[0]
 for time in times_spent:
        if time < min_value:
           min_value = time
           print("The minimum time spent was " + str(min_value))

    
#Linear Search in arrays of records
def linear_search(record):
    item_searching = int(input("Enter the value to find "))
    index = 0
    for i in range(0, len(record)):
        if item_searching == record[i].time:
            index = i
            print("Time", item_searching,"hours was spent by", record[index].name ,"during", record[index].activity  )
    
#count occourances in arrays of records
def count_occourances(record):
    item_counting = int(input("Enter the item to count "))
    count = 0
    name_count = []
    for i in range(0, len(record)):
        if item_counting == record[i].time :
            count = count +1
            name_count.append(record[i].name )
    print("Time", item_counting,"hours appeared", count,"times. Students", name_count)


    

StudentNames: ["Alice", "Ben", "Cara", "David", "Eva"]
Activities: ["hillwalking", "canoeing", "climbing", "hillwalking", "canoeing"]
times_spent = [5, 3, 4, 6, 5]
find_max(times_spent)
find_min(times_spent)
linear_search(record)
count_occourances(record)
