import json
from pathlib import Path

filepath = Path("data.json")

contacts = {
    1:["Anna", 23456789],
    2:["Bjørn", 99887766],
    3:["Clara", 11223344]
}


def load(data):
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        data = {int(key): value for key, value in data.items()}

    except FileNotFoundError:
        data = {}
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    return data
    

    

def save(contacts):
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)

def add():
    print("\n------------------")
    print("Add contact")
    name = input("Input name: ")
    number = getnumber()
    if number == False:
        return
    number=int(number)
    try:
        for i in contacts:
            continue
        i=i+1
    except:
        i = 0

    contacts[i] = [name, number]

    print(f"Tilføjede nummer - {name}, {number}")           
    return


def getnumber():
    x = False
    while True:
        number = input("Input number - 8 digits: ")
        if number == "Q":
            number=False
            break
        i = len(number)
        if i==8: 
            x=True 
        else: 
            x=False
        if x== True:
            try:
                int(number)
                break
            except: 
                print("Wrong input - write a number")
        print("Wrong input - write a number with 8 digits")
    return number



def find():
    print("\n------------------")
    print("Find contact")
    print("------------------")
    while True:
        print("\n1. Find via number")
        print("2. Find via name")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "3":
            break
        elif choice == "2":
            x = finder(1)
            if x == False:
                print("Den findes ikke")
            else:
                print("\nDen findes")
                print(contacts.get(x))
            break
        elif choice == "1":
            x = finder(2)
            if x == False:
                print("Den findes ikke")
            else:
                print("\nDen findes")
                print(contacts.get(x))
            break
    back()

def finder(option):
    if option==1:
        inp=input("Write name:")
        for i in contacts:
            liste=contacts.get(i)
            if inp == liste[0]:
                return i
        return False

    elif option==2: 
        inp=getnumber()
        inp = int(inp)
        for i in contacts:
            liste=contacts.get(i)
            if inp == liste[1]:
                return i
        return False


def showall(contacts):
    print("\n------------------")
    print("All contacts")
    print("------------------")
    if contacts == None:
        print("Der er ingen")
    else:
        for navn, nummer in contacts.items():
            print(f"{navn}: {nummer}")

    back()

def remove(contacts):
    print("\n------------------")
    print("Fjern contact")
    print("------------------")
    while True:
        print("\n1. Find via number")
        print("2. Find via name")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "3":
            break
        elif choice == "2":
            x = finder(1)
            if x == False:
                print("Den findes ikke")
            else:
                kon = contacts.pop(x)
                print("Fjernede kontakt:", kon)
            break
        elif choice == "1":
            x = finder(2)
            if x == False:
                print("Den findes ikke")
            else:
                kon = contacts.pop(x)
                print("Fjernede kontakt:", kon)
            break
    back()

def back():
    print(" ")
    input("Press enter to continue")
    return

#loader alle kontakter fra json fil
contacts = load(contacts)

while True:
    print("\n1. Add contact")
    print("2. Find contact")
    print("3. Show all contacts")
    print("4. Fjern contact")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "5":
        save(contacts)
        break
    elif choice == "4":
            remove(contacts)
    elif choice == "3":
        showall(contacts)
    elif choice == "2":
        find()
    elif choice == "1":
        add()
    else:
        print("------------------------")
        print("Wrong input please type a number")
        print("------------------------")

