#AncientReport

import argparse
import csv

#Input - filename, month, arguments
#python report.py database.csv april

def main():
    parser = argparse.ArgumentParser(description="A script to process birthday and anniversary reports.")
    parser.add_argument("filename", help="Path to the CSV file")
    parser.add_argument("month", help="Month to filter data (e.g., april)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    args = parser.parse_args()

    # Process the CSV file
    process_csv(args.filename, args.month, args.verbose)

def process_csv(filename, month, verbose):

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

    birthday_total = 0
    anniversary_total = 0
    department_count_birthday = {}
    department_count_anniversary = {}
    birthday_names = []
    anniversary_names = []

    for row in reader:
        birthday = row['Birthday']
        if month.lower() in birthday.lower():
            birthday_total+=1
            department = row['Department']
            department_count_birthday[department] = department_count_birthday.get(department, 0) + 1
        if verbose:
            birthday_name = row['Name']
            birthday_names.append(birthday_name)

        anniversary = row['Hiring']
        if month.lower() in anniversary.lower():
            anniversary_total+=1
            department = row['Department']
            department_count_anniversary[department] = department_count_anniversary.get(department, 0) + 1
        if verbose:
            anniversary_name = row['Name']
            anniversary_names.append(anniversary_name)

    if verbose:
        print(f'Report for {month} generated"\n"--- Birthdays ---"\n"Total: {birthday_total}"\n"By department:"\n"{department_count_birthday}"\n"Birthday Birds:"\n"{str(birthday_names)}"\n"--- Anniversaries ---"\n"Total: {anniversary_total}"\n"By department:{department_count_anniversary}"\n"Anniversary Birds:"\n"{str(anniversary_names)}')
    else:
        print(f'Report for {month} generated"\n"--- Birthdays ---"\n"Total: {birthday_total}"\n"By department:"\n"{department_count_birthday}"\n"--- Anniversaries ---"\n"Total: {anniversary_total}"\n"By department:{department_count_anniversary}')

    
#Output - Birthdays (total and by department) and Anniversaries (total and by department)
#if verbose than print the names

# Ensure the main function is executed when the script runs directly
if __name__ == "__main__":
    main()