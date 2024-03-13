from tkinter import *
import sys

root = Tk()


root.geometry('142x280+150+200') 
root.title("Style Demo") #specifying title of the program
#root.wm_iconbitmap('brush1.ico')#changing the default icon
#root.overrideredirect(1) # remove the root border - 
root.configure(background='#4D4D4D')#top level styling
# connecting to the external styling optionDB.txt
#root.option_readfile("designDB.txt")

mytext = Text(root, background='#101010', foreground="#D6D6D6",
borderwidth=18, relief='sunken', width=16, height=5 )
mytext.insert(END, "Style is knowing \nwho you are, what \nyou want to say, \nand not giving a \ndamn.")
mytext.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

Button(root, text='*' ).grid(row=1, column=1)
Button(root, text='^' ).grid(row=1, column=2)
Button(root, text='#' ).grid(row=1, column=3)
Button(root, text='<' ).grid(row=2, column=1)
Button(root, text='OK', cursor='target').grid(row=2, column=2)
Button(root, text='>').grid(row=2, column=3)
Button(root, text='+' ).grid(row=3, column=1)
Button(root, text='v', font='Verdana 8').grid(row=3, column=2)
Button(root, text='-' ).grid(row=3, column=3)
for i in range(0,10,1):
    Button(root, text=str(i) ).grid( column=3 if i%3==0 else (1 if i%3==1 else 2), row= 4 if i<=3 else (5 if i<=6 else 6))
#styling with built-in bitmap images
mybitmaps = ['info', 'error', 'hourglass', 'questhead', 'question','warning']
for i in mybitmaps:
    Button(root, bitmap=i, width=20,height=20).grid(row=(mybitmaps.index(i)+1), column=4,sticky='nw')

root.mainloop()