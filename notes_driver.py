from datetime import date


def add_todo(message,todo_list):
    dt=date.today()
    message="Date : "+dt.strftime('%d/%m/%Y')+"<br />"+message
    todo_list.append(message)

def remove_todo(position,todolist):
    del todolist[position-1]


def show_todo(todo_list):
    todo_string="#".join(todo_list)
    return todo_string