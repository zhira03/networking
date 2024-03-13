from tkinter import *
from turtle import color

from pyparsing import col

base1 = Tk()

base1.title("Calculator")

entry_field1 = Entry()
entry_field2 = Entry()
result_label = Label(text=f" ")

topFrame = Frame(base1)
display1 = Text(topFrame, background="grey", foreground="green",name="i fill up this space").grid(row=1, column=1)

bottomFrame = Frame(base1)
#clearScreen = Button(bottomFrame, text="C", background="red")
#divideSign = Button(bottomFrame, text="/",background="red")
#percentageSign = Button(bottomFrame, text="%",background="red")
#times_Sign = Button(bottomFrame, text="*",background="red")
#equals_Sign = Button(bottomFrame, text="=").grid(row=7, column=2)
for i in range(0,10,1):
    Button(bottomFrame, text=str(i) ).grid( column=3 if i%3==0 else (1 if i%3==1 else 2), row= 4 if i<=3 else (5 if i<=6 else 6))
numZero = Button(bottomFrame, text="0").grid(column=3, row=7)

topFrame.grid(row=1, column=1)
bottomFrame.grid(row=2, column=1, rowspan=7 , sticky=W)

#addition etc logic and positioning
add_button =Button(base1, text="+", background="red",command=lambda: calculate("add")).grid(row=7, column=1, sticky=W)
subtract_button =Button(base1, text="-", background="red", command=lambda: calculate("subtract")).grid(row=2, column=2, sticky=W)
multiply_button =Button(base1, text="*", background="red", command=lambda: calculate("multiply")).grid(row=2, column=3, sticky=W)
divide_button =Button(bottomFrame, text="/", background="red",command=lambda: calculate("divide")).grid(row=2, column=1, sticky=W)

#logic funtions
def calculate(operation):
    num1 = float(entry_field1.get())
    num2 = float(entry_field2.get())

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "divide":
        if num2 == 0:
            pass
        else:
            result = float(num1 / num2)
    elif operation == "multiply":
        result = float(num1 * num2)
    
    result_label.config(text=f"Result: {result}")



base1.mainloop()