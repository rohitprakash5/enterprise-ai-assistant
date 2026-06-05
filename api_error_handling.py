import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response.raise_for_status()

    users = response.json()

    print(f"Retrieved {len(users)} users")

except Exception as e:

    print("API call failed")
    print(e)