from functions import *
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("GUI на Python")
root.geometry("450x400")



messageName = StringVar()
messageDate = StringVar()


def intValue():
    if messageDate.get() == "":
        insertValue(messageName.get())
    else:
        insertValue(messageName.get(), messageDate.get())

message_info = Label(text = "Название")
message_info.place(relx = ".3", rely = ".1", anchor = "c", y = "15")
message_info = Label(text = "Дата")
message_info.place(relx = ".7", rely = ".1", anchor = "c", y = "5")

message_info = Label(text = "(****-**-**)")
message_info.place(relx = ".7", rely = ".1", anchor = "c", y = "20")

message_name = Entry(textvariable = messageName, bg="#00FFEA")
message_name.place(relx = ".3", rely = ".2", anchor = "c")
message_date = Entry(textvariable = messageDate, bg="#00FFEA")
message_date.place(relx = ".7", rely = ".2", anchor = "c")

message_button = Button(text = "Добавить", bg = "#000000", fg= "#DCFAFF",
                         activebackground="#5D1820", command = intValue,
                         activeforeground ="#4B75FF")
message_button.place(relx = ".2", rely = ".3", anchor = "c")
message_button = Button(text = "Найти",bg = "#000000", fg= "#DCFAFF",
                         activebackground="#5D1820",
                         activeforeground ="#4B75FF")
message_button.place(relx = ".4", rely = ".3", anchor = "c")
message_button = Button(text = "Изменить",bg = "#000000", fg= "#DCFAFF",
                         activebackground="#5D1820", 
                         activeforeground ="#4B75FF")
message_button.place(relx = ".6", rely = ".3", anchor = "c")
message_button = Button(text = "Удалить", bg = "#000000", fg= "#DCFAFF",
                         activebackground="#5D1820", 
                         activeforeground ="#4B75FF")
message_button.place(relx = ".8", rely = ".3", anchor = "c")

root.mainloop()

