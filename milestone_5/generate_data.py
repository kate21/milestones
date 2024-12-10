#AncientDataGenerator

import random
import csv
import os

name_pool = ["Sergio", "Vasiliy", "Giovanni", "Anna", "Dario", "Kateryna", "Peter", "Agnes"]
surname_pool = ["Velaskez", "Nikitenko", "Otti", "Carrol", "Campanez", "Sylvia", "Degtiarenko", "Radchenko"]
month_pool = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
department_pool = ["sales", "marketing", "rnd", "communication"]

data_list = []
#n is a number of employees
n=100

for i in range(n):
    employee_name = random.choice(name_pool)+ " " + random.choice(surname_pool)
    employee_birthday = random.choice(month_pool)+" " + str(random.randint(1,28))
    employee_department = random.choice(department_pool)
    employee_hiring_date = random.choice(month_pool)+" " + str(random.randint(1,28))
    employee_data = {
        'Name' : employee_name,
        'Birthday' : employee_birthday,
        'Department' : employee_department,
        'Hiring' : employee_hiring_date
    }
    data_list.append(employee_data)

#print(data_list)

with open("database.csv", "w") as file:
  header = ['Name','Birthday','Department', 'Hiring']
  writer = csv.DictWriter(file, fieldnames = header)

  writer.writeheader()
  writer.writerows(data_list)

  #to check
with open("database.csv", "r") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)
print("Current working directory:", os.getcwd())