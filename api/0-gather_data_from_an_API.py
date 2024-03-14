#!/usr/bin/python3
"""
First module to work with flask api apps
"""
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

        # Setting variables for printing
        EMPLOYEE_NAME = user_json["name"]
        NUMBER_OF_DONE_TASKS = sum(1 for task in todos_json
                                   if str(task["userId"]) == user_id
                                   and task["completed"] is True)
        TOTAL_NUMBER_OF_TASKS = sum(1 for task in todos_json
                                    if str(task["userId"]) == user_id)

        # Printing employee info and task titles
        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in todos_json:
            if str(task["userId"]) == user_id and task["completed"] is True:
                print(f"\t {task['title']}")


if __name__ == "__main__":
    Get_Todo().todo()
