import csv
def read_profiles():
    employees=[]
    with open('emp.csv','r',newline='',encoding ='utf-8')as file:
        csv_reader=csv.DictReader(file) 
        for row in csv_reader:
            employees.append(row)
    return employees

def print_employee(emp):
    #print(emp)
    print(f'Name: {emp["name"]}')
    print(f'Age: {emp["age"]}')
    print(f'Job Title: {emp["job_title"]}')
    
employees=read_profiles()
for emp in employees:
    print_employee(emp)
    print('-' * 40)
