from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

from pyrsistent import v

root = Tk()
root.geometry("720x500")
menubar = Menu(root)

#menubar item creation
filemenu = Menu(menubar, tearoff=0)
edit_button = Menu(menubar, tearoff=0,)
view_button = Menu(menubar, tearoff=0)
about_button = Menu(menubar, tearoff=0)
help_button = Menu(menubar, tearoff=0)
themes_menu = Menu(view_button, tearoff=0)

#all the functions i used to create the files, undo actions, pull the images etc
def open_file():
    global filename
    filename = filedialog.askopenfilename(defaultextension=".txt",filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
    if filename == "": 
        filename = None 
    else:
        root.title(os.path.basename(filename) + " - Taku's App Bishhhh!! LOL") 
        writing_pad.delete(1.0,END)
        fh = open(filename,"r")
        writing_pad.insert(1.0,fh.read())
        fh.close()

def save():
    global filename
    try:
        pulled_file = open(filename, 'w')
        text_writen = writing_pad.get(1.0, 'end')
        pulled_file.write(text_writen)
        pulled_file.close()
    except:
        save_as()

def save_as():
    try:
        pulled_file = filedialog.asksaveasfilename(initialfile ='Filename.txt', defaultextension=".txt",
                                                   filetypes=[("AllFiles","*.*"),("Text Documents","*.txt")])
        fh = open(pulled_file, 'w')
        textoutput = writing_pad.get(1.0, END)
        fh.write(textoutput)
        fh.close()
        root.title(os.path.basename(pulled_file) + " - pyPad")
    except:
        pass

def new_file():
    global filename
    root.title("Untitled")
    filename = None
    writing_pad.delete(1.0,END)

def line_number_updater(event=None):
    phrase = ""
    if showln.get():
        endline, endcolumn = writing_pad.index('end-1c').split('.')
        phrase = '\n'.join(map(str, range(1, int(endline))))
        current_line, current_column = writing_pad.index("insert").split(".")
        infor_bar.config(text=f"Line: {current_line} | Column: {current_column}")
    ln_lable.config(text=phrase, anchor = NW)


def hightlight_line():
    writing_pad.tag_remove('active_line', 1.0 , 'end')
    writing_pad.tag_add('active_line', 'insert linestart', 'insert line-end+1c')
    writing_pad.after(start_highlight)

def start_highlight(event=None):
    val = hi_light_line.get()
    undo_highlight() if not val else hightlight_line()

def undo_highlight():
        writing_pad.tag_remove("active_line", 1.0, "end")

def show_info_bar():
    val = showInfoBar.get()
    if val:
        infor_bar.pack(expand=NO, fill=None, side=RIGHT, anchor=SE)
    elif not val:
        infor_bar.pack_forget()

def help_box():
    mess = ( " hey there")
    messagebox.showwarning("Help", mess)
    
def exit_app(event = None):
    if messagebox.askokcancel("Quit", "Do you really want to ditch?"):
        save()
        root.destroy()
    root.protocol("WM_DELETE_WINDOW")

    
def cut():
    writing_pad.event_generate("<<Cut>>")
    line_number_updater()

def copy():
    writing_pad.event_generate("<<Copy>>")
    line_number_updater()

def paste():
    writing_pad.event_generate("<<Paste>>")
    line_number_updater()

def undo():
    edit_button.event_add("<<Undo>>")
    line_number_updater()

def redo():
    edit_button.event_generate("<<Redo>>")
    line_number_updater()

def select_all():
    writing_pad.tag_add("sel", "1.0", "end")


class SearchHandler:
    def __init__(self):
        self       

    def find(self):
        self.small_find_window = Toplevel(root)
        self.small_find_window.title("Find")
        self.small_find_window.geometry("262x65+200+250")
        self.small_find_window.transient(root)
        Label(self.small_find_window, text="Find All: ").grid(row=0, column=0,sticky=E)
        self.find_all_var = StringVar
        self.entry_var = Entry(self.small_find_window, width=25, textvariable=self.find_all_var)
        self.entry_var.grid(row=0, column=1, padx=2, pady=2, sticky=NSEW)
        self.entry_var.focus_set()
        self.num_var = IntVar
        Checkbutton(self.small_find_window, text="Ignore Case", variable=self.num_var).grid(row=1, column=1, sticky=E, padx=2, pady=2)
        Button(self.small_find_window, text="Find All", underline=0, 
            command=lambda:self.search_for(self.find_all_var.get(), self.num_var.get(),self.writing_pad, 
                                           self.small_find_window, self.entry_var)
            ).grid(row=0, column=2, sticky=E + W, padx=2, pady=2)

        def end_search():
            self.writing_pad.tag_remove("match", "1.0",END)
            self.small_find_window.destroy()

        def search_for(needle, case_sensitive):
            self.writing_pad.tag_remove('match', '1.0', END)
            count =0
            if needle:
                pos = '1.0'
            while True:
                pos = writing_pad.search(needle, pos, nocase=case_sensitive, stopindex=END)
                if not pos:
                    break
            lastpos = f'{pos} {len(needle)}' 
            self.writing_pad.tag_add('match', pos, lastpos)
            count += 1
            pos = lastpos
            writing_pad.tag_config('match', foreground='red', background='yellow')
            self.entry_var.focus_set()
            self.small_find_window.title(f"{count} matches found")

search_handler = SearchHandler()

def theme_selector():
    global background_col, foreground_col
    val = theme_color.get()
    colors = color_options.get(val)
    foreground_col ,background_col = colors.split(".")#failing to split. None type error thrown
    foreground_col ,background_col = '#'+foreground_col, '#'+background_col
    writing_pad.config(bg=background_col, fg=foreground_col)

#adding functionalitily
#file menu
filemenu.add_command(label="New",command=new_file, accelerator="Ctrl + N", compound=LEFT, underline=0)
filemenu.add_command(label="Open", accelerator="Ctrl + O", compound=LEFT, command=open_file)
filemenu.add_command(label="Save", accelerator="Ctrl + S", compound=LEFT, command= save)
filemenu.add_command(label="Save As", accelerator="Ctrl + Alt + S", compound=LEFT, command=save_as)
filemenu.add_command(label="Close", accelerator="Ctrl + W", compound=LEFT)
filemenu.add_command(label="Close All", accelerator="Ctrl + Shift + W", compound=LEFT)
filemenu.add_command(label="Exit", accelerator="Alt + F4", compound=LEFT, command=exit_app)


#edit menu
edit_button.add_command(label="Undo", accelerator="Ctrl + Z", compound=LEFT,command=undo)
edit_button.add_command(label="Redo", accelerator="Ctrl + Y", compound=LEFT, command=redo)
edit_button.add_separator()
edit_button.add_command(label=" Cut", accelerator="Ctrl + X", compound=LEFT, command=copy)
edit_button.add_command(label="Copy", accelerator="Ctrl + C", compound=LEFT, command=cut)
edit_button.add_command(label="Paste", accelerator="Ctrl + V", compound=LEFT, command=paste)
edit_button.add_separator()
edit_button.add_command(label="Find", accelerator="Ctrl + F", compound=LEFT, underline=0, command=lambda: search_handler())
edit_button.add_separator()
edit_button.add_command(label="Select All", accelerator="Ctrl + A", compound=LEFT, underline=0, command=select_all)

#view menu
showln = IntVar()
showln.set(1)
hi_light_line = IntVar()
showInfoBar = IntVar()
showInfoBar.set(1)
view_button.add_checkbutton(label="Show Line Number", variable=showln)
view_button.add_checkbutton(label="Show info Bar at the Bottom", variable=showInfoBar)
view_button.add_checkbutton(label="Highlight Line", variable=hi_light_line)
view_button.add_cascade(label="Themes", menu=themes_menu)

#view menu extending into themes_menu
color_options = {
'1. Default White': '000000.FFFFFF',
'2. Greygarious Grey':'83406A.D1D4D1',
'3. Lovely Lavender':'202B4B.E1E1FF' , 
'4. Aquamarine': '5B8340.D1E7E0',
'5. Bold Beige': '4B4620.FFF0E1',
'6. Cobalt Blue':'ffffBB.3333aa',
'7. Olive Green': 'D1E7E0.5B8340',
}
theme_color = StringVar()
theme_color.set('1. Default White')
for choice in sorted(color_options):
    themes_menu.add_checkbutton(label=choice, variable= theme_color, command= theme_selector)
menubar.add_cascade(label="View", menu= view_button)


#help menu
help_button.add_command(label="Send FeedBack", compound=LEFT, underline=0)
help_button.add_command(label="View Help", compound=LEFT, underline=0, command=help_box)


#making them visible
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=edit_button)
menubar.add_cascade(label="View", menu=view_button)
menubar.add_cascade(label="About" , menu=about_button)
menubar.add_cascade(label="Help" , menu=help_button)

#shortcuts
short_cut_bar = Frame(root, height=25, bg="light sea green")
icons = {"newFile.png","save.png"}
"""
for i, icon in enumerate(icons):
    try: 
        useIcon = PhotoImage(file = 'C:\\Users\\HP\\Desktop\\VisualStudio coding\\networking\\tkinterApps\\icons')
        action1 = eval(icon)
        tool_bar = Button(short_cut_bar, image=useIcon, command=action1)
        tool_bar.image_names(useIcon)
        tool_bar.pack(side=LEFT)
    except PermissionError:
        print("Permission not granted. Run as Administrator")
"""    
short_cut_bar.pack(expand=NO, fill=X)
ln_lable = Label(root, width=5, bg="antique white")
ln_lable.pack(side=LEFT, anchor=NW, fill=Y)

#text widget and scroll widget
writing_pad = Text(root, undo=TRUE, font="Arial")
writing_pad.pack(expand=YES, fill=BOTH)
scrolling = Scrollbar(writing_pad)
writing_pad.config(yscrollcommand=scrolling.set)
scrolling.config(command=writing_pad.yview)
scrolling.pack(side=RIGHT, fill=Y)

#line info widget
infor_bar = Label(writing_pad, text="Line: 1 | Column: 0")
infor_bar.pack(expand=NO, fill=None, side=RIGHT, anchor=SE)

writing_pad.bind("<Any-KeyPress>", line_number_updater)
writing_pad.tag_config("active_line", background="ivory2")
root.config(menu=menubar)

root.mainloop()