def getnumber(digits):
    x = False
    while True:
        number = input(f"Input number - {digits} digits: ")
        if number == "Q":
            number=False
            break
        i = len(number)
        if i==digits: 
            x=True 
        else: 
            x=False
        if x== True:
            try:
                int(number)
                break
            except: 
                print("Wrong input - write a number")
        print(f"Wrong input - write a number with {digits} digits")
    return number

def checknumber(number, digits):
    valid = False
    try:
        i = len(number)
    except:
        i = len(str(number))
    
    if i==digits: 
        valid=True 
    else: 
        valid=False
        return valid
    if valid==True:
        try:
            int(number)
            valid=True
        except: 
            valid=False
    return valid