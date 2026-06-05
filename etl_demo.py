import requests

def extract():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data")

def transform(users):
        transformed_users=[]
        for user in users:
            transformed_users.append({
                "name": user["name"],
                "company": user["company"]["name"],
                "user_count": len(user["name"]),
                "email": user["email"]
            })
        return transformed_users

def load(users):    
    for user in users:
        print(f"{user['name']} works at {user['company']} and has {user['user_count']} characters in their name. Contact: {user['email']}")

if __name__ == "__main__":
    try:
        users = extract()
        transformed_users = transform(users)
        load(transformed_users)
    except Exception as e:
        print("ETL failed")
        print(e)
