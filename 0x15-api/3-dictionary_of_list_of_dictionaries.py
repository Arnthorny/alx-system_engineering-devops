#!/usr/bin/python3
"""
Python script that, using a REST API,
for all employees, returns information
about his/her TODO list progress and exports to a json file.
"""
import json
import requests


def get_all_emp_todos():
    """
    This function returns a list of todos for all users

    Return:
        (`list`): List of objects containg all user's todos.
    """
    todo_ep = 'https://jsonplaceholder.typicode.com/todos'
    r_todo = requests.get(todo_ep)
    res_json_arr = r_todo.json()
    return (res_json_arr)


def populate_all_emp_dict(all_u_json, all_todos):
    all_dict = {}

    for user in all_u_json:
        u_name = user.get('username')
        u_id = user.get('id')
        tmp_u_obj = [{'username': u_name, 'task': t.get('title'),
                      'completed': t.get('completed')} for t in all_todos
                     if t.get('userId') == u_id]
        all_dict[u_id] = tmp_u_obj

    return all_dict


def main():
    """
    This function starts the script by querying a user's id
    from the given user endpoint.
    """
    all_user_ep = 'https://jsonplaceholder.typicode.com/users'

    r = requests.get(all_user_ep)
    all_u_json = r.json()

    all_emp_todos = get_all_emp_todos()
    all_emp_dict = populate_all_emp_dict(all_u_json, all_emp_todos)

    with open(f"todo_all_employees.json", 'w') as o_file:
        json.dump(all_emp_dict, o_file)


if __name__ == "__main__":
    main()
