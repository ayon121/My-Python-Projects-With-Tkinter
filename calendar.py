from datetime import date
from tkinter import *
from tkcalendar import *


#creating root display
root = Tk()
root.geometry("350x350")
root.title("calendar made by Ayon saha")
root.config(bg="lightblue")
root.resizable(False,False)


#creating calendar
mycal = Calendar(root,setmode= "day" , date_pattern = "d/m/yy")
mycal.pack (padx = 20 , pady= 15)

#defining fuction for the date selection
def date_select():
    mydate = mycal.get_date()
    selectedDate = Label (text= mydate ,borderwidth=3, relief=GROOVE )
    selectedDate.pack (padx= 3 , pady= 3)

#creating button for date selection
my_button = Button (root, text= "Select Date" ,borderwidth=3, relief=RAISED, command= date_select)
my_button.pack(padx= 15 , pady= 15)

#this the mainloop of the programm
root.mainloop()
