from tkinter import *

cabin = Tk()
randLabel = Label(cabin, text=" Click here").pack()

def mycallBack(event):
    print(dir(event))
    print("you clicked at ", event.x, event.y)

myFrame = Frame(cabin, bg="grey", width=130, height=80)
myFrame.bind("<Button-1>", mycallBack)
myFrame.pack()

cabin.mainloop()