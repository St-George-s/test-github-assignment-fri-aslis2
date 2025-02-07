import csv 

company = []
numEmployees = []
ceoSalary = []

def read_data():
    with open("coursework software/2024/companies.csv", 'r' ) as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
           
        return company, numEmployees, ceoSalary
    

#main
read_data()
    
