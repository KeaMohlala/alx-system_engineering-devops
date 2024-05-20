#!/usr/bin/python3
"""
script to get employee TODO list progress from REST API using
employee ID and export data to CSV file
"""
import csv
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


def export_to_csv(user, todos):
    """
    saves employee progress from the API to CSV file
    """
    filename = f"{user['id']}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(
                file, quotechar='"', quoting=csv.QUOTE_ALL
        )

        for todo in todos:
            writer.writerow(
                    [user['id'], user['username'],
                        todo['completed'], todo['title']]
            )


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except IndexError:
        print("Usage:./script_name.py <employee_id>")
        sys.exit(1)

    user, todos = fetch_employee_todos(employee_id)
    export_to_csv(user, todos)
