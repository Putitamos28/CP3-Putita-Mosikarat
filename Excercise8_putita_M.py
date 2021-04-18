usernameInput = input("username :")
passwordInput = input("password :")
if usernameInput == "kamputii" and passwordInput == "098273" :
    print("Log-in complete!!")
    print("Welcome to Putita Cafe")
    print("---------- Menu -----------")
    print("1. Ice Americano : 50 BATH")
    print("2. Ice Chocolate : 55 BAHT")
    print("3. Espresso      : 55 BATH")
    UserSelect = int(input("What do you want>>"))
    if UserSelect == 1:
        print("Ice Americano")
        price = int(input("Price :"))
        amount = int(input("Amount :"))
        result = price*amount
        print(result)
    elif UserSelect == 2:
        print("Ice Chocolate")
        price = int(input("Price :"))
        amount = int(input("Amount :"))
        result = price*amount
        print(result)
    elif UserSelect == 3:
        print("Espresso")
        price = int(input("Price :"))
        amount = int(input("Amount :"))
        result = price*amount
        print(result)
    else:
        print("No Drinks")
else:
    print("Sorry!! --Your Username or Password is incorrect--")
