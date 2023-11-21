import functions
import PySimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter a ToDo: ", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My ToDo App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()