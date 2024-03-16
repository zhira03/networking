from tkinter import *

root = Tk()
root.geometry("900x100")
menubar = Menu(root)

#menubar item creation
filemenu = Menu(menubar, tearoff=0)
edit_button = Menu(menubar, tearoff=0,)
view_button = Menu(menubar, tearoff=0)
about_button = Menu(menubar, tearoff=0)
themes_menu = Menu(view_button, tearoff=0)

#all the functions i used to create the files, undo actions, pull the images etc
def new_file():
    print("Placeholder for now!")

def cut():
    writing_pad.event_generate("<<Cut>>")

def copy():
    writing_pad.event_generate("<<Copy>>")

def paste():
    writing_pad.event_generate("<<Paste>>")

def undo():
    edit_button.event_add("<<Undo>>")

def redo():
    edit_button.event_generate("<<Redo>>")

def select_all():
    writing_pad.tag_add("sel", "1.0", "end")

def find():
    find_all_var = StringVar
    entry_var = Entry(small_find_window, width=25, textvariable=find_all_var)
    small_find_window = Toplevel(root)
    small_find_window.title("Find")
    small_find_window.geometry("262x65+200+250")
    small_find_window.transient(root)
    Label(small_find_window, text="Find All: ").grid(row=0, column=0,sticky=E)
    entry_var.grid(row=0, column=1, padx=2, pady=2, sticky=WE)
    entry_var.focus_set()
    num_var = IntVar
    Checkbutton(small_find_window, text="Ignore Case", variable=num_var).grid(row=1, column=1, sticky=E, padx=2, pady=2)
    Button(small_find_window, text="Find All", underline=0, 
           command=lambda:search_for(find_all_var.get(), num_var.get(),writing_pad, small_find_window, entry_var)
           ).grid(row=0, column=2, sticky=E + W, padx=2, pady=2)

    def end_search():
        writing_pad.tag_remove("match", "1.0",END)
        small_find_window.destroy()

    def search_for(needle, cssnstv, writing_pad, small_find_window, entry_var):
        writing_pad.tag_remove()

#adding functionalitily
#file menu
filemenu.add_command(label="New",command=lambda:new_file, accelerator="Ctrl + N", compound=LEFT, underline=0)
filemenu.add_command(label="Open", accelerator="Ctrl + O", compound=LEFT)
filemenu.add_command(label="Save", accelerator="Ctrl + S", compound=LEFT)
filemenu.add_command(label="Save All", accelerator="Ctrl + Alt + S", compound=LEFT)
filemenu.add_command(label="Close", accelerator="Ctrl + W", compound=LEFT)
filemenu.add_command(label="Close All", accelerator="Ctrl + Shift + W", compound=LEFT)

#edit menu
edit_button.add_command(label="Undo", accelerator="Ctrl + Z", compound=LEFT,command=undo)
edit_button.add_command(label="Redo", accelerator="Ctrl + Y", compound=LEFT, command=redo)
edit_button.add_separator()
edit_button.add_command(label=" Cut", accelerator="Ctrl + X", compound=LEFT, command=copy)
edit_button.add_command(label="Copy", accelerator="Ctrl + C", compound=LEFT, command=cut)
edit_button.add_command(label="Paste", accelerator="Ctrl + V", compound=LEFT, command=paste)
edit_button.add_separator()
edit_button.add_command(label="Find", accelerator="Ctrl + F", compound=LEFT, underline=0, command=find)
edit_button.add_separator()
edit_button.add_command(label="Select All", accelerator="Ctrl + A", compound=LEFT, underline=0, command=select_all)

#view menu
view_button.add_checkbutton(label="Show Line Number")
view_button.add_checkbutton(label="Show info Bar at the Bottom")
view_button.add_cascade(label="Themes", menu=themes_menu)
#view menu extending into themes_menu
themes_menu.add_radiobutton(label="1. Default White")
themes_menu.add_radiobutton(label="2. Dracular Night")
themes_menu.add_radiobutton(label="3. System Theme")
themes_menu.add_radiobutton(label="4. Monotone")


#making them visible
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=edit_button)
menubar.add_cascade(label="View", menu=view_button)

#shortcuts
short_cut_bar = Frame(root, height=25, bg="light sea green")
short_cut_bar.pack(expand=NO, fill=X)
in_lable = Label(root, width=2, bg="antique white")
in_lable.pack(side=LEFT, anchor=NW, fill=Y)

#text widget and scroll widget
writing_pad = Text(root, undo=TRUE)
writing_pad.pack(expand=YES, fill=BOTH)
scrolling = Scrollbar(writing_pad)
writing_pad.config(yscrollcommand=scrolling.set)
scrolling.config(command=writing_pad.yview)
scrolling.pack(side=RIGHT, fill=Y)


root.config(menu=menubar)

root.mainloop()