# need to extract data from api https://jsonplaceholder.typicode.com/users 
# and save it in csv file with name users.csv with columns name,email,company,city 
import requests
import csv
response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code == 200:
    data = response.json()
    with open('users_report.csv', mode='w', newline='') as file:
        fieldnames = ['name', 'email', 'company', 'city']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for user in data:
            csv_writer.writerow({
                "name": user["name"],
                "email": user["email"],
                "company": user["company"]["name"],
                "city": user["address"]["city"]
            })
    print("CSV file created successfully with API data.")

    record_count = len(data)
    print(f"Total records written to CSV: {record_count}")