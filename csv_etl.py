import csv 

def get_experienced_band(experience):
    if experience >= 15:
        return "Expert"
    elif experience >= 10:
        return "Senior"
    elif experience >= 5:
        return "Mid-Level"
    else:
        return "Junior"

def get_salary_band(salary): 
    if salary >= 150000:
        return "High"
    elif salary >= 80000 :
        return "Medium"
    else:
        return "Low" 

employees = []

with open('employees.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        row["experience"] = int(row["experience"])
        row["band"] = get_experienced_band(row["experience"])
        row["salary"] = int(row["salary"])
        row["salary_band"] = get_salary_band(row["salary"])
        employees.append(row)

with open('employees_enriched.csv', mode='w', newline="") as file:
    fieldnames = ['name', 'experience','salary', 'band','salary_band']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(employees)
    
    print("csv file created successfully with enriched data.")
