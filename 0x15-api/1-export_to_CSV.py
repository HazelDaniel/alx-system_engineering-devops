#!/usr/bin/python3
"""this module uses the requests module to get the number of
    todos of an employee based on the ID provided
    and also creates a CSV file to hold a records
    based on the data retrieved"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) < 2:
        exit(98)

    employee_id = sys.argv[1]
    user_todos_completed = []
    user_todos = []
    user_name = ""

    def fetch_and_catch(url, func):
        """this function fetches a resource
            from a url with error handling enabled"""
        base_url = "https://jsonplaceholder.typicode.com/"
        response = requests.get(f"{base_url}{url}")
        if response.status_code == 200:
            try:
                data = response.json()
                if data:
                    func(data)
            except Exception as e:
                print(e)
        else:
            print(f"Failed to fetch resource. Error code:"
                  f"{response.status_code}")

    def set_user_name(data):
        """a sub-routine that sets the user data"""
        global user_name
        user_name = data.get("username", "")

    def set_todos(data):
        """a sub-routine that sets the todos of a user"""
        global user_todos
        global user_todos_completed
        user_todos = data
        user_todos_completed = [x for x in data if x.get('completed', False)]

    fetch_and_catch(f"users/{employee_id}/todos", set_todos)
    fetch_and_catch(f"users/{employee_id}", set_user_name)

    tasks_complete = len(user_todos_completed)
    all_tasks = len(user_todos)
    try:
        records = []
        with open(f"{employee_id}.csv", "w") as file:
            records = [(f"\"{employee_id}\"", f"\"{user_name}\"",
                        f"\"{entry.get('completed', 'False')}\"",
                        f"\"{entry.get('title', '')}\"")
                       for entry in user_todos]
            records = [",".join(val) for val in records]
            for val in records:
                serial_val = json.dumps(val)
                file.write(f"{val}\n")
    except Exception as e:
        print(e)
