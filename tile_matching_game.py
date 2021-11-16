from tkinter import * 
from tkinter import messagebox
from typing import get_origin
import random

#root is our main display 
root = Tk()
root.title ("Tile matching game made by Ayon saha")
root.geometry("600x600")

#create button frame
my_frame = Frame(root)
my_frame.pack(pady= 30)

def match_number():
    global matches
    #create matches
    matches= [1,1,2,2,3,3,4,4,5,5,6,6]
    #Shuffle our matches
    random.shuffle(matches)

#creating winner to find winner
global winner
winner = 0
#defing winner function
def win():
    my_label.config (text= "Congratulation you win")
    button_list = [b1 ,b2 , b3 , b4 , b5 , b6 , b7 ,b8 ,b9 , b10 ,b11 ,b12]
    #creating a loop for changing button color
    for button in button_list:
        button.config(bg= "yellow")
    messagebox.showinfo("TILE MATCHING GAME made by Ayon Saha" , "TO PLAY AGAIN RESET THE GAME")

#Defining some veriable
count = 0
answer_list = []
answer_dict = {}


#difining fucntion for button click
def button_click(b , number):
    global count , answer_list , answer_dict , winner

    if b ["text"] == " " and count < 2 :
        b ["text"] = matches[number]
        #add number toanswer list
        answer_list.append(number)
        #add button and number to answer dict
        answer_dict[b]= matches[number] 
        #Incremnt our counter
        count += 1


    #start to determine  correct or not
    if len(answer_list)== 2 :
        if matches[answer_list[0]] == matches [answer_list[1]]:
            my_label.config (text= "YEAPS... MATCH")

            #creting a loop for disabling button after clicking
            for key in answer_dict :
                key ["state"] = "disabled"
            
            #difining everything back to nothing
            count= 0
            answer_list = []
            answer_dict = {}
            #increment winner counter
            winner += 1
            if winner == 6:
                win()

        else:
            my_label.config(text = "TRY AGAIN")

            count= 0
            answer_list = []
            
            #pop up box
            for key in answer_dict :
                key ["text"] = " "

            answer_dict = {}

def reset():
    global b1 ,b2 ,b3, b4 ,b5 , b6 , b7 , b8, b9, b10 ,b11 ,b12
    global matches , winner
    my_label.config(text = "GAME STARTS")
    winner = 0
    #calling match number fuction for 
    match_number()

    #defining button
    b1 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b1 , 0))
    b2 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b2 , 1))
    b3 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b3 , 2))
    b4 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b4 , 3))
    b5 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b5 , 4))
    b6 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b6 , 5))
    b7 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b7 , 6))
    b8 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b8 , 7))
    b9 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b9 , 8))
    b10 = Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b10 , 9))
    b11= Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b11 , 10))
    b12= Button(my_frame , text= " " ,font= ("Helvetica", 20), height= 2, width= 6 ,borderwidth=2,relief=RIDGE, command= lambda: button_click(b12 , 11))

    #showing button
    b1.grid(row=0 , column= 0)
    b2.grid(row=0 , column= 1)
    b3.grid(row=0 , column= 2)
    b4.grid(row=0 , column= 3)


    b5.grid(row=1 , column= 0)
    b6.grid(row=1 , column= 1)
    b7.grid(row=1 , column= 2)
    b8.grid(row=1 , column= 3)


    b9.grid(row=2 , column= 0)
    b10.grid(row=2 , column= 1)
    b11.grid(row=2 , column= 2)
    b12.grid(row=2 , column= 3)


#difing label for showing result of the game
my_label = Label(root , text ="GAME STARTS", font= ("Helvetice", 30), border= 4, relief=GROOVE )
my_label.pack(pady= 20)


#making a manu
my_menu = Menu(root)
root.config(menu= my_menu)

options_menu = Menu (my_menu , tearoff= False)
my_menu.add_cascade(label="MENU" , menu= options_menu)
options_menu.add_command(label = "Reset game" , command = reset)
options_menu.add_command(label= "EXIT" ,command= root.quit)

#calling reset function for start the game
reset()

#it is the mainloop of the proggram
root.mainloop()
