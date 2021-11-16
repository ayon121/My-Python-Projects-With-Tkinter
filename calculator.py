#It is my python project
#In this project I will make a calcator

#import tkinter
from tkinter import *
#root is our main display
root = Tk()
root.title ("Caculator")

#In tkiner we use "ëntry" to take input
e = Entry (root, width=50,borderwidth = 5 ,bg = "black" , fg= "white")
#here we are display our entry button
e.grid(row= 0,column = 0 , columnspan = 3,padx= 10 , pady = 10)

#defning button click function
def button_click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
 
#defining clear button
def button_clear():
    e.delete(0, END)


#defining summation button
def button_summation():
    first_number = e.get()
    global f_num
    global math 
    math = "summation"
    f_num = int(first_number)
    e.delete(0, END)

#defining  division button
def button_division():
    first_number = e.get()
    global f_num
    global math 
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#defining minus button
def button_minus():
    first_number = e.get()
    global f_num
    global math 
    math = "minus"
    f_num = int(first_number)
    e.delete(0, END)


#defining multipication button
def button_multipication():
    first_number = e.get()
    global f_num
    global math 
    math = "multipication"
    f_num = int(first_number)
    e.delete(0, END)


#defining modulo button
def button_modulo():
    first_number = e.get()
    global f_num
    global math 
    math = "modulo"
    f_num = int(first_number)
    e.delete(0, END)

#defining power button
def button_power():
    first_number = e.get()
    global f_num
    global math 
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)



#defining equal button
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "summation":
        e.insert (0, f_num + int(second_number))
    elif math == "division":
        e.insert (0, f_num / int(second_number))
    elif math == "minus":
        e.insert (0, f_num - int(second_number))
    elif math == "modulo":
        e.insert (0, f_num % int(second_number))
    elif math == "power":
        e.insert (0, f_num ** int(second_number))
    else:
        e.insert (0, f_num * int(second_number))
    




#difning the buttons
mybutton_1 = Button (root , text= "      1      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(1))
mybutton_2 = Button (root , text= "      2      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(2))
mybutton_3 = Button (root , text= "      3      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(3))
mybutton_4 = Button (root , text= "      4      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(4))
mybutton_5 = Button (root , text= "      5      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(5))
mybutton_6 = Button (root , text= "      6      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(6))
mybutton_7 = Button (root , text= "      7      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(7))
mybutton_8 = Button (root , text= "      8      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(8))
mybutton_9 = Button (root , text= "      9      " ,borderwidth=5,relief=RIDGE, padx = 20 ,pady = 20 , command= lambda: button_click(9))
mybutton_10 = Button (root , text= "   0   " ,borderwidth=5,relief=RIDGE, padx = 140 ,pady = 20 , command= lambda: button_click(0))

#mathematical button creating
mybutton_summation = Button (root , text= " + " ,borderwidth=5,relief=RIDGE,padx = 35 ,pady = 20 , command=button_summation)
mybutton_division = Button (root , text= "  /  " ,borderwidth=5,relief=RIDGE, padx = 35 ,pady = 20 , command= button_division)
mybutton_minus = Button (root , text= " - " ,borderwidth=5,relief=RIDGE, padx = 35 ,pady = 20 , command= button_minus)
mybutton_multipication = Button (root , text= "  X " ,borderwidth=5,relief=RIDGE, padx = 35 ,pady = 20 , command= button_multipication)
mybutton_modulo = Button (root , text= " % " ,borderwidth=5,relief=RIDGE,padx = 35 ,pady = 20 , command= button_modulo)
mybutton_power = Button (root , text= "x^X" ,borderwidth=5,relief=RIDGE, padx = 35 ,pady = 20 , command= button_power)



#clear and equal button creating
mybutton_clear = Button (root , text= "Clear" ,borderwidth=9,relief=RIDGE, padx = 140 ,pady = 20 , command=button_clear)
mybutton_equal = Button (root , text= "   =   " ,borderwidth=9,relief=RIDGE, padx = 140 ,pady = 20 , command= button_equal)


#showing the buttons
mybutton_1.grid(row=1, column=0)
mybutton_2.grid(row=1, column=1)
mybutton_3.grid(row=1, column=2)


mybutton_4.grid(row=2, column=0)
mybutton_5.grid(row=2, column=1)
mybutton_6.grid(row=2, column=2)

mybutton_7.grid(row=3, column=0)
mybutton_8.grid(row=3, column=1)
mybutton_9.grid(row=3, column=2)

mybutton_10.grid(row=4,column=0,columnspan= 3)

#showing mathematical buttons
mybutton_summation.grid(row=5,column=0)
mybutton_division.grid(row=5,column=1)
mybutton_minus.grid(row=5,column=2)

mybutton_multipication.grid(row=6,column=0)
mybutton_modulo.grid(row=6,column= 1)
mybutton_power.grid(row=6, column= 2)

#clear and equal button
mybutton_clear.grid(row=7,column=0 ,columnspan= 3)
mybutton_equal.grid(row=8,column=0 , columnspan= 3)



root.mainloop()
