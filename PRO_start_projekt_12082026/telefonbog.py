contacts = {
    1:["Anna", 23456789],
    2:["Bjørn", 99887766],
    3:["Clara", 11223344]
}

def add():
    print("\n------------------")
    print("Add contact")
    name = input("Input name: ")
    number = getnumber()
    if number == False:
        return
    number=int(number)
    
    for i in contacts:
        continue
    i=i+1

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
            x = find2(1)
            if x == False:
                print("Den findes ikke")
            else:
                print("\nDen findes")
                print(contacts.get(x))
            break
        elif choice == "1":
            x = find2(2)
            if x == False:
                print("Den findes ikke")
            else:
                print("\nDen findes")
                print(contacts.get(x))
            break
    back()

def find2(option):
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
    for navn, nummer in contacts.items():
        print(f"{navn}: {nummer}")

    back()

def back():
    print(" ")
    input("Press button to continue")
    return




while True:
    print("\n1. Add contact")
    print("2. Find contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "4":
        break
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

