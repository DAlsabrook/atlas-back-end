#!/usr/bin/python3
"""
Module to import an api and export a csv file of user info
"""
import csv
import requests
import sys

# Get args from cmd line and set variables
args = sys.argv
print(len(args))
if len(args) == 2:
    user_id = args[1]
url = "https://jsonplaceholder.typicode.com/"

# Get api to json in a variable
user_result = requests.get(url + "users/" + user_id)
todos_result = requests.get(url + "todos")
user_json = user_result.json()
todos_json = todos_result.json()

# Get specific user information and task assigned to them
username = user_json["username"]
user_tasks_list = [task for task in todos_json if str(task["userId"]) == user_id]

# Write specific user information to a csv file
filename = f"{user_id}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for task in user_tasks_list:
        writer.writerow([user_id, username, task["completed"], task["title"]])
