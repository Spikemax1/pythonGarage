#!/usr/bin/env python

import csv
import os
import datetime

FILENAME = "docs/products.csv"

def createFile():
    if not os.path.isfile(FILENAME):
        Newname = "Название"
        Newdate = "Дата"
        with open(FILENAME, "w", newline = "", encoding = "utf8") as file:
            writeNames = csv.writer(file)
            writeNames.writerow([Newname, Newdate]) 

try:
    if os.path.isfile(FILENAME):
        print("Указанный файл существует")
    else:
        if os.path.exists("docs/"):
            createFile()
        else:
            os.mkdir("docs/")
            createFile()            
except: 
    print("Не удалось создать файл")
    exit()
      


def insertValue(intData, intTime = datetime.date.today()):
    intData = intData.lower().strip()
    with open(FILENAME, "a", encoding = "utf8") as file:
            writeNames = csv.writer(file)
            writeNames.writerow([intData, intTime])
    
def searchInt(name):
    name = name.lower().strip()
    with open(FILENAME, "r") as file:
        freader = csv.reader(file)
        for row in freader:
            if row[0] == name:
                elem = [row[0], row[1]]
    return elem

def deleteInt(name):
    elem = searchInt(name)
    with open("docs/products2.csv", 'w', newline = "") as newFile:
        writer = csv.writer(newFile)
        with open(FILENAME, "r", newline = "") as file:
            freader = csv.reader(file)
            for row in freader:
                model = [row[0], row[1]]
                if model == elem:
                    continue
                writer.writerow(model)
    os.remove("docs/products.csv")
    os.rename("docs/products2.csv", "docs/products.csv")





