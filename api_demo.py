import requests

response=requests.get("https://jsonplaceholder.typicode.com/users")

print("Status Code:", response.status_code)

users = response.json()

#print(users[0])
#for user in users:
#    print(user["name"])
#print("Total Users:", len(users))
#print("First User:", users[0]["name"])
#print("Company Name:", users[0]["company"]["name"])

for user in users:
    print(f"{user['name']} works at {user['company']['name']}")


