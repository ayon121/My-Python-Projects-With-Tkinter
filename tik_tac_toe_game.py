from tkinter import *
from tkinter import messagebox
from typing import get_origin

#root is our main display 
root = Tk()
root.title ("Tic-Tac-Toe made by Ayon Saha")

#create a manu
my_menu = Menu(root)
root.config(menu= my_menu)

#disable all button
def disableallbutton():
    button1.config(state= DISABLED)
    button2.config(state= DISABLED)
    button3.config(state= DISABLED)
    button4.config(state= DISABLED)
    button5.config(state= DISABLED)
    button6.config(state= DISABLED)
    button7.config(state= DISABLED)
    button8.config(state= DISABLED)
    button9.config(state= DISABLED)

#X starts so true
clicked = True
count = 0

#check the game
def check():
    global winner
    winner = False
###################check for x wins#################
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg= "red")
        button2.config(bg= "red")
        button3.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg= "red")
        button5.config(bg= "red")
        button6.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()
    
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg= "red")
        button8.config(bg= "red")
        button9.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg= "red")
        button4.config(bg= "red")
        button7.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()
    
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg= "red")
        button5.config(bg= "red")
        button8.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg= "red")
        button6.config(bg= "red")
        button9.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg= "red")
        button5.config(bg= "red")
        button9.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg= "red")
        button5.config(bg= "red")
        button7.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "X WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

###########check for O wins#########

    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg= "red")
        button2.config(bg= "red")
        button3.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg= "red")
        button5.config(bg= "red")
        button6.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()
    
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg= "red")
        button8.config(bg= "red")
        button9.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg= "red")
        button4.config(bg= "red")
        button7.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()
    
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg= "red")
        button5.config(bg= "red")
        button8.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS\n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg= "red")
        button6.config(bg= "red")
        button9.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg= "red")
        button5.config(bg= "red")
        button9.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS\n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()

    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg= "red")
        button5.config(bg= "red")
        button7.config(bg= "red")
        winner = True
        messagebox.showinfo("TIK TAC TOE" , "O WINS \n TO PLAY ANOTHER MATCH PLEASE RESET THE GAME")
        disableallbutton()
################check is it tie ######
    if count == 9 and winner == False:
        messagebox.showinfo("TIK TAC TOE" , "NO ONE WINS \n LET'S PLAY AGAIN \n PLEASE RESET THE GAME")


#button fuction 
def button_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
       b["text"] = "X"
       clicked = False
       count += 1
       check()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check()
    else:
        messagebox.showerror("TIK TAC TOE" , "This box is already \n Plz choose another box")


#reset fuction
def reset():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    global clicked, count
    clicked = True
    count = 0
    #Building button
    button1 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button1))
    button2 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button2))
    button3 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button3))
    button4 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button4))
    button5 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button5))
    button6 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button6))
    button7 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button7))
    button8 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE, command= lambda: button_click(button8))
    button9 = Button(root, text= " " , font=("Helvetica",20),height=3,width=6, bg= "white" ,borderwidth=7,relief=RIDGE,command= lambda: button_click(button9))


    #showing button
    button1.grid(row=0 , column= 0)
    button2.grid(row=0 , column= 1)
    button3.grid(row=0 , column= 2)

    button4.grid(row=1 , column= 0)
    button5.grid(row=1 , column= 1)
    button6.grid(row=1 , column= 2)

    button7.grid(row=2 , column= 0)
    button8.grid(row=2 , column= 1)
    button9.grid(row=2 , column= 2)

#creaing manu options
options_menu = Menu (my_menu , tearoff= False)
my_menu.add_cascade(label="MENU" , menu= options_menu)
options_menu.add_command(label = "Reset game" , command = reset)

#calling reset fucntion to start the game
reset()
#it is the mainloop of the proggram
root.mainloop()
