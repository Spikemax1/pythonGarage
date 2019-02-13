from tkinter import *
import random

count = 0
koloda = [2,3,4,5,6,7,8, 9, 10, "валет", "дама","король", "туз"] * 4
random.shuffle(koloda)
def take():
    global count
    

root = Tk()
root.title("Gui на Python")
root.geometry("300x250")

text1 = Label(root, text = "Игра в BlackJack", bg = "#8bb1ef",
                    fg = "#5e3404", justify = CENTER)
text1.place(x = 100, y = 0)

text2 = Label(root, text = "Карта", bg = "#8afcc1",
                    fg = "#0a0a0a")
text2.place(x = 120, y = 50)

btn1 = Button(text= "Взять", command = take)
btn1.place(x = 40, y = 100)

btn2 = Button(text= "Хватит", command = take)
btn2.place(x = 200, y = 100)

text3 = Label(root, text = "Количество Очков", bg = "#050505",
                    fg = "#007bff")
text3.place(x = 90, y = 150)

root.mainloop()