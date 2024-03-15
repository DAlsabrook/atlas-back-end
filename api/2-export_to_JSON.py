#!/usr/bin/python3
"""
First module to work with flask api apps
"""
import json
import requests
import sys


class Get_Todo():
    """class to get employee information
    """

    def todo(self):
        args = sys.argv
        user_id = args[1]
        url = "https://jsonplaceholder.typicode.com/"

        # Get api to json locally stored
        user_result = requests.get(url + "users/" + user_id)
        todos_result = requests.get(url + "todos")
        user_json = user_result.json()
        todos_json = todos_result.json()

        # Setting up anf formatting new json
        user_dict = {}
        user_tasks_list = []
        tmp_dict = {}
        for task in todos_json:
            if str(task["userId"]) == user_id:
                tmp_dict["task"] = task["title"]
                tmp_dict["completed"] = task["completed"]
                tmp_dict["username"] = user_json["username"]
                user_tasks_list.append(tmp_dict)
                tmp_dict = {}
        user_dict[user_json["id"]] = user_tasks_list

        # Exporting user info to json file
        filename = f"{user_id}.json"
        with open(filename, mode='w') as file:
            json.dump(user_dict, file)


if __name__ == "__main__":
    Get_Todo().todo()
