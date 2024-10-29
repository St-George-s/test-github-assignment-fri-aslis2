import csv 

studentID = ["S001", "S002", "S003", "S004"]
firstName = ["Alice", "Bob", "Charlie", "Diana"]
lastName = ["Johnson", "Smith"]
grade = ["A", "B", "A", "C"]

class Student:
    def __init__(self, studentID, firstName, lastName, grade):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade 

def readStudentData():
    students = []
    with open("student.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
            student = Student(row[0], row[1], row[2], row[3], int(row[4]))
            students.append(student)

    return students

students = readStudentData()
print(students[0].studentID, students[0].firstName, students[0].lastName, students[0].grade)