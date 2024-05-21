#!/usr/bin/python3
"""
script to fetch all employee tasks
"""
import json
import requests


def fetch_users():
    """
    Fetches all users from the API
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()
    return users


def fetch_employee_todos(employee_id):
    """
    fetches employee todo list using employee id as parameter
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch todo items
    todos_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todos = todos_response.json()

    return todos


def collect_all_todos(users):
    """
    Collects todos for all employees
    """
    all_todos = {}
    for user in users:
        employee_id = user['id']
        todos = fetch_employee_todos(employee_id)
        for todo in todos:
            task_title = todo['title']
            task_completed = todo['completed']
            username = user['username']
            entry = {
                    "username": username, "task": task_title,
                    "completed": task_completed
            }
            if employee_id not in all_todos:
                all_todos[employee_id] = []
            all_todos[employee_id].append(entry)
    return all_todos


def main():
    """
    main entry point of module
    """
    users = fetch_users()
    all_todos = collect_all_todos(users)
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(all_todos, outfile, indent=4)


if __name__ == "__main__":
    main()
