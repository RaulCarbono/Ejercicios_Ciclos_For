userDb = ('rack')
passwordDb = ("hola5")
balance = float(5000000)

def validateuser(user,password):
    if user == userDb and password == passwordDb:
        return True 
    return False

def login():
    print ("welcome ")
    user = input("enter user ")
    password = input("enter password ")
    return validateuser(user,password )

def remove(value):
    if value > balance: 
        return False, balance
    return True, balance - value

def toDeposite(value):
    return True, balance + value

def action(option): 
    if option == 1:
        value = int(input("enter value to deposite "))
        return toDeposite(value)
    if option == 2:
        value = int(input("entrer value to remove"))
        return remove(value)
    return False, balance

def run():
    if not login():
        print("user or password invalid")
        return
    print("What would you like to do? ")
    option = int(input("1. for to deposite or 2.for remove "))
    ok, value = action(option)
    if not ok: 
        print("the action was not performed value: ", value)
    else: 
        print("the action performed corretly")

run()