import re
with open('staffdata.txt','r') as f:
    data = f.read()
    datas = f.readlines()
    split_data = re.findall(r'\w+', data)
    sorted_names = sorted(split_data[1::4])

def start():
    print(data)
    start = input("1. New Staff\n2. Delete Staff\n3. View Summary Data\n4.Save and Exit\nInput Choice:").lower()
    while True:
        if start == "1":
            newstaff()
            newstaffname()
            newstaffposition()
        if start == "2":
            pass
        if start == "3":
            pass
        if start == "4":
            pass
        elif start == "exit":
            exit()
def newstaff():
    text = str(input("Please input Staff ID:"))
    split_data.append(text)
    if text =="stop":
        start()
    if len(text) != 5:
        return False
    if input == input:
        return False
    if text(0) != "S":
        return False
    if text(1) != int:
        return False
    else:
        start()  
def newstaffname():
    nameinput=(input("Please input a name:"))
    split_data.append(nameinput)
    if nameinput =="stop":
        start()
    if len(nameinput) <= 20:
        return False
def newstaffposition():
    posinput=(input("Please choose a position:"))
    if posinput == "Staff":
        return True
    if posinput == "Manager":
        return True
    if posinput == "Officer":
        return True
    else:
        return False
class Employee:
    def __init__(self,id,name,position,salary):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salary = salary

start()