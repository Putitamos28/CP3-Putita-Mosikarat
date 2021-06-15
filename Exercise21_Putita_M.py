from tkinter import *
import math
def leftClickButton(event):
    print(float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    labelResult.configure(text= float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    Check()
def Check():
    resultcheck = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    if resultcheck >= 30:
        result = "อ้วนมาก"
    elif resultcheck >= 25.0:
        result = "อ้วน"
    elif resultcheck >= 23:
        result = "น้ำหนักเกิน"
    elif resultcheck >= 18.6:
        result = "น้ำหนักปกติและเหมาะสม"
    else:
        result = "ผอมเกินไป"
    labelResult.configure(text = result)

MainWindow = Tk()
labelHeight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0, column =0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row = 0, column =1)
labelWeight = Label(MainWindow, text = "น้ำหนัก (Kg.)")
labelWeight.grid(row = 1, column =0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1, column = 1)
calculateButton = Button(MainWindow, text = "คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column = 0)
labelResult = Label(MainWindow, text = "ผลลัพธ์")
labelResult.grid(row = 2, column =1)
MainWindow.mainloop()