from tkinter import *
from tkinter import filedialog

root = Tk()

#it will set the geametry
root.geometry("600x600")

#it is he title of the GUI
root.title ("Notepad made by Ayon saha")

#it will fixed the GUI
root.config(bg = "lightgreen")

#for this size can be changed
root.resizable(False,False)

#defining save file function
def save_file():
    open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
    if open_file is None:
        return
    text= str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close() 

#defining open file function
def open_file():
    file= filedialog.askopenfile(mode= "r" , filetypes= [("text files", ".txt")])
    if file is not None:
        content= file.read()
    entry.insert(INSERT, content)

#defining save file button
my_button1 = Button (root , width= "20" , height= "2" , bg= "black" , fg= "white" , text= "save file" ,borderwidth=3,relief=RAISED, command= save_file )
my_button1.place(x= 100 , y= 5)

#defining open file button
my_button2 = Button (root, width= "20", height= "2" , bg= "black" , fg= "white" , text= "open file" ,borderwidth=3,relief=RAISED, command= open_file )
my_button2.place(x=300 , y= 5)

#defining entry for text
entry = Text(root , width= "70" , height= "40" , wrap= WORD , borderwidth= 6)
entry.place(x= 10 , y= 60)


#it the main loopof the proggram
root.mainloop()
