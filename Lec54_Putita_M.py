def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234" :
        return showMenu()
    else:
        print("Your username or password incorrect")
        return login()
def showMenu():
    print("----- iShop ------")
    print("1. Vat Calaulator")
    print("2. Price Calaulator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1 :
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2 :
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print (price1 + price2)
    else :
        return showMenu()
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)
login()