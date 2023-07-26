import csv

def student_table(name, students):
    count = 0
    for student in students:
        if student == name:
            count += 1
    if count == 0:
        students.append({'student_name': name})

def house_table(house, head, houses):
    count = 0
    for h in houses:
        if h['house'] == house:
            count += 1
    if count == 0:
        houses.append({'house': house, "head": head})

def relation_table(, students):
    count = 0
    for student in students:
        if student == name:
            count += 1
    if count == 0:
        students.append({'student_name': name})

students = []
houses = []
relations = []

with open('students.csv','r') as students_csv:
    reader = csv.DictReader(students_csv)
    for row in reader:
        name = row['student_name']
        house = row['house']
        head = row['head']

        student_table(name, students)
        house_table(house, head, houses)
