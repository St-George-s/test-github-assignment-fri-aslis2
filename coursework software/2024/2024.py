import csv 

company = []
numEmployees = []
ceoSalary = []

def read_data():
    with open("coursework software/2024/companies.csv", 'r' ) as file:
        reader = csv.reader(file)
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
           
        return company, numEmployees, ceoSalary

def find_maxsalary_difference(company, ceoSalary):
   companyCheck = input("Enter the name of the company you would like to check:")
   #Find the highest CEO salary 
   max_value = ceoSalary[0] 
   max_index = 0
   for counter in range(1, len(ceoSalary)):
        if ceoSalary[counter] > max_value:
            max_value = ceoSalary[counter]
            max_index = counter 
   print(company[max_index] + " company has the highest paid CEO")
   
   #Find difference in CEO salary between highest salary and the company to check  
   if companyCheck in company:
       companyCheck_index = company.index(companyCheck)
       difference = max_value - ceoSalary[companyCheck_index]
       print("The " + companyCheck + " CEO earns " + str(difference) + " less than the highest paid CEO ")
   else:
       print("Company not found")

def find_max_employees(numEmployees):
    max_value = numEmployees[0] 
    max_index = 0
    for counter in range(1, len(numEmployees)):
        if numEmployees[counter] > max_value:
            max_value = numEmployees[counter]
            max_index = counter
    print("The highest number of employees employed by a single company is " + str(max_value))

    found = 0 
    for employees in numEmployees:
        if employees <= 0.1 * max_value:
            found += 1 
    print(str(found) + " companies employ within 10% of " + str(max_value))


   
    
    

#main
read_data()
find_maxsalary_difference(company, ceoSalary)
find_max_employees(numEmployees)
    
