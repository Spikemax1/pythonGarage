from functions import *
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI на Python")
root.geometry("450x400")

messageName = StringVar()
messageDate = StringVar()

message_info = Label(text = "Название")
message_info.place(relx = ".3", rely = ".1", anchor = "c", y = "15")
message_info = Label(text = "Дата")
message_info.place(relx = ".7", rely = ".1", anchor = "c", y = "15")

message_name = Entry(textvariable = messageName, bg="#eff0f2")
message_name.place(relx = ".3", rely = ".2", anchor = "c")
message_date = Entry(textvariable = messageDate, bg="#eff0f2")
message_date.place(relx = ".7", rely = ".2", anchor = "c")

message_button = Button(text = "Добавить", command = insertValue)
message_button.place(relx = ".2", rely = ".3", anchor = "c")
message_button = Button(text = "Найти")
message_button.place(relx = ".4", rely = ".3", anchor = "c")
message_button = Button(text = "Изменить")
message_button.place(relx = ".6", rely = ".3", anchor = "c")
message_button = Button(text = "Удалить")
message_button.place(relx = ".8", rely = ".3", anchor = "c")

root.mainloop()