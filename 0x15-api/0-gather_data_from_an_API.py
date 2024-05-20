#!/usr/bin/python3
"""
script to get employee TODO list progress from REST API using
employee ID
"""
import requests
import sys


def fetch_employee_todos(employee_id):
    """
    fetches employee todo list using employee id as parameter
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user = user_response.json()

    # Fetch todo items
    todos_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todos = todos_response.json()

    return user, todos


def print_todo_progress(user, todos):
    """
    prints employee progress using the user and todos info
    fetched from the API
    """
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(
        f"Employee {user['name']} is done with "
        f"tasks({completed_count}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except IndexError:
        print("Usage:./script_name.py <employee_id>")
        sys.exit(1)

    user, todos = fetch_employee_todos(employee_id)
    print_todo_progress(user, todos)
