import requests

todo_id = input("Enter a todo ID: ")

url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print("Title:", data["title"])
    print("Completed:", data["completed"])

except requests.exceptions.RequestException as error:
    print("Something went wrong:", error)