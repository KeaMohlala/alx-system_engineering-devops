#!/usr/bin/python3
"""
script to get employee TODO list progress from REST API using
employee ID and export data to JSON file
"""
import json
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


def export_to_json(user, todos):
    """
    saves employee progress from the API to JSON format
    """
    filename = f"{user['id']}.json"
    data = {}
    data[user['id']] = []

    for todo in todos:
        data[user['id']].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        })

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except IndexError:
        print("Usage:./script_name.py <employee_id>")
        sys.exit(1)

    user, todos = fetch_employee_todos(employee_id)
    export_to_json(user, todos)
