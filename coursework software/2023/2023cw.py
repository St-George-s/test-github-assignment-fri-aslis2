import csv 

attraction = []
category = []
visitors = []
days_open = []
height = []

def read_data():
    with open("coursework/2023/test.csv", 'r' ) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            attraction.append(row[0])
            category.append(row[1])
            visitors.append(int(row[2]))
            days_open.append(int(row[3]))
            height.append(row[4])

        return attraction, category, visitors, days_open, height

def find_max(attraction, visitors):
    max_value = visitors[0] 
    max_index = 0
    for counter in range(1, len(visitors)):
        if visitors[counter] > max_value:
            max_value = visitors[counter]
            max_index = counter
    print("The most visited attraction is " + attraction[max_index] + " with " + str(max_value) + " visitors ")
    return attraction[max_index], visitors

def find_min(attraction, visitors):
    min_value = visitors[0] 
    min_index = 0
    for counter in range(1, len(visitors)):
        if visitors[counter] > min_value:
            min_value = visitors[counter]
            min_index = counter
    print("The least visited attraction is " + attraction[min_index] + " with " + str(min_value) + " visitors")
    return attraction[min_index], visitors

def findRollerCoastersService(attraction, category, days_open):
    # Create ‘service.csv’ file 
    with open("service.csv", "w") as file:
     for i in range (0,len(attraction)):
         if category[i] == "Roller Coaster":
             days = days_open[i] % 90
             if 90 - days <= 7:
                 file.write(attraction[i])

    # 3.2 Loop for each attraction 
    # 3.3  If current category is ‘Roller Coaster’ then 
    # 3.4   Set days to current daysOpen modulus 90 
    # 3.5   If (90 – days) is less than or equal to 7 then 3.6    Write current attraction to file 3.7   End if 
    # 3.8  End if 
    # 3.9 End loop 3.10  Close ‘service.csv’ file

#main
read_data()
find_max(attraction, visitors)
find_min(attraction, visitors)
findRollerCoastersService(attraction, category, days_open)