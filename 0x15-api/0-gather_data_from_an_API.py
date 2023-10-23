#!/usr/bin/python3
"""
Python script that, using a REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
from functools import reduce
import requests
import sys


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
    done = reduce(lambda x, y: x + y.get('completed'), emp_todos, 0)
    total = len(emp_todos)
    print(f'Employee {u_json.get("name")} is done with tasks({done}/{total}):')
    for todo in emp_todos:
        print(f'\t {todo.get("title")}')


if __name__ == "__main__":
    main()
