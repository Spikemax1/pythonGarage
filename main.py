from functions import *
from tkinter import *
from tkinter import messagebox
import datetime

root = Tk()
root.title("GUI на Python")
root.geometry("450x400")



messageName = StringVar()
messageDate = StringVar()
resultText = StringVar()



def intValue():
    if messageDate.get() == "":
        insertValue(messageName.get())
    else:
        insertValue(messageName.get(), messageDate.get())

def searchVal():
    elem = searchInt(messageName.get())
    newDate = datetime.datetime.now()
    '''
    dateStr = elem[1].split("-")
    oldDate = datetime.date(int(dateStr[0]), int(dateStr[1]), int(dateStr[2]))
    '''
    if elem == False:
        resultText.set("Пусто")
        return False
    oldDate = datetime.datetime.strptime(elem[1], "%Y-%m-%d")
    result = (newDate - oldDate).days
    val = datetime.timedelta(days= result)
    print(val)    
    resultText.set(val)

def changeVal():
    changeInt(messageName.get(), messageDate.get())

def deleteVal():
    deleteInt(messageName.get())

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
                         activebackground="#5D1820", command = searchVal,
                         activeforeground ="#4B75FF")
message_button.place(relx = ".4", rely = ".3", anchor = "c")
message_button = Button(text = "Изменить",bg = "#000000", fg= "#DCFAFF",
                         activebackground="#5D1820", command = changeVal,
                         activeforeground ="#4B75FF")
message_button.place(relx = ".6", rely = ".3", anchor = "c")
message_button = Button(text = "Удалить", bg = "#000000", fg= "#DCFAFF",
                         activebackground="#5D1820", command = deleteVal,
                         activeforeground ="#4B75FF")
message_button.place(relx = ".8", rely = ".3", anchor = "c")

message_result = Label(textvariable = resultText, bg = "#818284", fg= "#e2fcbf",
                         activebackground="#5D1820",
                         activeforeground ="#4B75FF")
message_result.place(relx = ".5", rely = ".5", anchor = "c")

root.mainloop()

