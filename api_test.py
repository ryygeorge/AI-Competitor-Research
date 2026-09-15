import requests

todo_id = input("Enter a todo ID: ")

url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

response = requests.get(url)

data = response.json()

print("Title:", data["title"])
print("Completed:", data["completed"])