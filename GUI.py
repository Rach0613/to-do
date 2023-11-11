import functions
import PySimpleGUI as sg

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter a ToDo: ")
add_button = sg.Button("Add")

window = sg.Window('My ToDo App', layout=[[label], [input_box, add_button]])
window.read()
window.close()


