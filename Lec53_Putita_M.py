totalPrice = int(input())
def vatCalculate(totalPrice):
    resalt = totalPrice+(totalPrice*7/100)
    return resalt
print(vatCalculate(totalPrice))