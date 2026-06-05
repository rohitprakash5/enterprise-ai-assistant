# need to extract data from api https://jsonplaceholder.typicode.com/users 
# and save it in csv file with name users.csv with columns name,email,company,city 
import requests
import csv

def extract():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to extract data from API")
        return []

def transform(data):
    transformed_data = []
    for user in data:
        transformed_data.append({
            "name": user["name"],
            "email": user["email"],
            "company": user["company"]["name"],
            "city": user["address"]["city"]
        })
    return transformed_data

def load(data):
    with open('users_report.csv', mode='w', newline='') as file:
        fieldnames = ['name', 'email', 'company', 'city']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for user in data:
            csv_writer.writerow(user)
        print("CSV file created successfully with API data.")

if __name__ == "__main__":
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

    record_count = len(transformed_data)
    print(f"Total records written to CSV: {record_count}")    