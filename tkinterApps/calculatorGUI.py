from tkinter import *
from turtle import color

from pyparsing import col

base1 = Tk()

base1.title("Calculator")

topFrame = Frame(base1)
result_label= Label(topFrame, text="")
firstNum = Entry(topFrame)
secNum =Entry(topFrame)

bottomFrame = Frame(base1)
#addition etc logic and positioning
add_button =Button(bottomFrame, text="+", background="red",command=lambda: calculate("add"))
subtract_button =Button(bottomFrame, text="-", background="red", command=lambda: calculate("subtract"))
multiply_button =Button(bottomFrame, text="*", background="red", command=lambda: calculate("multiply"))
divide_button =Button(bottomFrame, text="/", background="red",command=lambda: calculate("divide"))

for i in range(0,10,1):
    Button(bottomFrame, text=str(i) ).grid( column=3 if i%3==0 else (1 if i%3==1 else 2), row= 4 if i<=3 else (5 if i<=6 else 6))
numZero = Button(bottomFrame, text="0").grid(column=3, row=7)

topFrame.grid(row=1, column=1, sticky=W)
bottomFrame.grid(row=2, column=1 , sticky=W)

#logic funtions
def calculate(operation):
    num1 = float(firstNum.get())
    num2 = float(secNum.get())

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "divide":
        if num1 | num2 == 0:
            result = "Can't divide by 0"
        else:
            result = float(num1 / num2)
    elif operation == "multiply":
        result = float(num1 * num2)
    
    result_label.config(text=f"Result: {result}")

#aesthetics
    #topFrame
result_label.grid(row=3, column = 2, columnspan=2)
firstNum.grid(row=1, column=1)
secNum.grid(row=1, column=3, padx=10)

    #bottomFrame
add_button.grid(row=7, column=1, sticky=W)
subtract_button.grid(row=2, column=2, sticky=W)
multiply_button.grid(row=2, column=3, sticky=W)
divide_button.grid(row=2, column=1, sticky=W)

base1.mainloop()
