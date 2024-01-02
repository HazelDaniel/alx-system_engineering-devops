#!/usr/bin/python3
"""this module uses the requests module to get the number of
    todos of an employee based on ID provided"""

if __name__ == "__main__":
    import requests
    import json

    users_dict = {}

    def fetch_and_catch(url, func, **kwargs):
        """this function fetches a resource
            from a url with error handling enabled"""
        base_url = "https://jsonplaceholder.typicode.com/"
        response = requests.get(f"{base_url}{url}")
        if response.status_code == 200:
            try:
                data = response.json()
                if data and kwargs:
                    func(data, **kwargs)
                elif data:
                    func(data)
            except Exception as e:
                print(e)
        else:
            print(f"Failed to fetch resource. Error code:"
                  f"{response.status_code}")

    def set_user_name(data):
        """a sub-routine that sets the user data"""
        global users_dict
        user_name = data.get("username", "")
        if user_name:
            users_dict[f"{data.get('id')}"] = user_name

    def set_todos(data, key=""):
        """a sub-routine that sets the todos of a user"""
        global users_dict
        user_todos = [{"task": f"{x.get('title', '')}",
                       "completed": x.get('completed', False),
                      "username":
                       f"{users_dict[f'{key}']}"}
                      for x in data]
        users_dict[f"{key}"] = user_todos

    def set_all_users(data):
        """ a sub-routine that sets all the users
            and their respective todos"""
        for i in data:
            set_user_name(i)
        for i in data:
            fetch_and_catch(f"users/{i.get('id', '')}/todos",
                            set_todos, key=i.get("id"))

    fetch_and_catch("users/", set_all_users)

    try:
        with open("todo_all_employees.json", "w") as file:
            res_dict = json.dumps(users_dict)
            file.write(res_dict)
    except Exception as e:
        print(e)
