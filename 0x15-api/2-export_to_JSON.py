#!/usr/bin/python3
"""
Python script that, using a REST API,
for a given employee ID, returns information
about his/her TODO list progress and exports to a json file.
"""
import json
import requests
import sys


def create_json(e_id, e_username, e_todos):
    """
    This function writes the employee's data to a json file
    Args:
        e_id(`string`):         Id of employee
        e_username(`string`):   Employe's username
        e_todos(`list`):        List of objects containing employee todos
    """
    u_ob = {e_id: []}
    with open(f"{e_id}.json", 'w') as o_file:
        u_ob[e_id] = [{'task': t.get('title'), 'completed': t.get('completed'),
                      'username': e_username} for t in e_todos]
        json.dump(u_ob, o_file)


def get_emp_todos(e_id):
    """
    This function returns a list of todos for a given user
    Args:
        e_id(string): String representing the user id

    Return:
        (`list`): List of objects containg given user's todos.
    """
    todo_ep = f'https://jsonplaceholder.typicode.com/todos?userId={e_id}'
    r_todo = requests.get(todo_ep)
    res_json_arr = r_todo.json()
    return (res_json_arr)


def main():
    """
    This function starts the script by querying a user's id
    from the given user endpoint.
    """
    emp_id = sys.argv[1]
    user_ep = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    r = requests.get(user_ep)
    u_json = r.json()

    emp_todos = get_emp_todos(emp_id)
    create_json(emp_id, u_json.get('username'), emp_todos)


if __name__ == "__main__":
    main()
