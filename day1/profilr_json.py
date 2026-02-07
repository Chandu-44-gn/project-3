
import json
def read_profiles():    
    with open('emp.json', 'r', encoding='utf-8') as file:
        employees = json.load(file)
    return employees

def print_employee(emp):
    #print(emp)
    print(f'Name: {emp["name"]}')
    print(f'Age: {emp["age"]}')
    print(f'Job Title: {emp["job_title"]}')

employees = read_profiles()
for emp in employees:
    print_employee(emp)
    print('-' * 40)
