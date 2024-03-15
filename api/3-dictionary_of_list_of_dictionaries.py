#!/usr/bin/python3
"""
First module to work with flask api apps
"""
import json
import requests


class Get_Todo():
    """class to get employee information
    """

    def todo(self):
        url = "https://jsonplaceholder.typicode.com/"

        # Get api to json locally stored
        user_result = requests.get(url + "users")
        todos_result = requests.get(url + "todos")
        user_json = user_result.json()
        todos_json = todos_result.json()

        # Setting up and formatting new json
        user_dict = {}
        for user in user_json:
            user_tasks_list = []
            tmp_dict = {}
            for task in todos_json:
                if task["userId"] == user["id"]:
                    tmp_dict["task"] = task["title"]
                    tmp_dict["completed"] = task["completed"]
                    tmp_dict["username"] = user["username"]
                    user_tasks_list.append(tmp_dict)
                    tmp_dict = {}
            user_dict[user["id"]] = user_tasks_list

        # Exporting user info to json file
        filename = "todo_all_employees.json"
        with open(filename, mode='w') as file:
            json.dump(user_dict, file)


if __name__ == "__main__":
    Get_Todo().todo()
