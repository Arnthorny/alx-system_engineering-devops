#!/usr/bin/python3
"""
Python script that, using a REST API,
for a given employee ID, returns information
about his/her TODO list progress and exports to a csv file.
"""
import csv
import requests
import sys


def create_csv(e_id, e_username, e_todos):
    """
    This function writes the employee's data to a csv file
    Args:
        e_id(`string`):         Id of employee
        e_username(`string`):   Employe's username
        e_todos(`list`):        List of objects containing employee todos
    """
    id_u = [e_id, e_username]
    with open(f"{e_id}.csv", 'w', newline='') as o_file:
        o_writer = csv.writer(o_file, quoting=csv.QUOTE_ALL)
        all_ro = [id_u + [t.get('completed'), t.get('title')] for t in e_todos]
        o_writer.writerows(all_ro)


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
    create_csv(emp_id, u_json.get('username'), emp_todos)


if __name__ == "__main__":
    main()
