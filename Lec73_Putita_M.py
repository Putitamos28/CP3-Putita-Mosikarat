systemMenu = {"ข้าวมันไก่ต้ม":40, "ข้าวมันไก่ทอด":45, "ข้าวมันผสม": 50}
menuList = []
def showBill():
    totalPrice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("Total :" , totalPrice)


while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()