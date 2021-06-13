menulist = []
pricelist = []

def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for number in range(len(menulist)):
        print(menulist[number], pricelist[number])
        totalPrice += int(pricelist[number])
    print("Total :", totalPrice)
while True :
    menuName = input("Plese Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menulist.append(menuName)
        pricelist.append(menuPrice)
showBill()