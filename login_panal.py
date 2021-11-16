#Here I am making a Log in panal with tkinter

#importing tkinter
from tkinter import *
from tkinter import messagebox

#making the GUI
root = Tk()
root.title ("Log in panal made by Ayon saha")
root.geometry("400x400")


#creating a label for text username and password 
my_label = Label(root, text = "    Type your username and password    ", font= ("Arial",8) , borderwidth=1 , relief= RIDGE)
my_label.place(x=105, y= 85)


#creating a label for username
my_label1 = Label(root, text = "Username", font= ("Courier",10))
my_label1.place(x=100, y= 120)

#creating alabel for password
my_label2 = Label(root, text= "Password" , font= ("Courier", 10))
my_label2.place(x= 100 , y= 160)


#taking entry for username
entry1 = Entry (root  ,borderwidth= 4)
entry1.place(x= 180 , y= 120)

#taking entry for password
entry2 = Entry (root  , borderwidth= 4)
entry2.place (x= 180 , y= 160)

#definging log in function
def login ():
    global entry1 , entry2
    username = entry1.get()
    password= entry2.get()

    if (username == "") and (password == "") :
        my_button.config(bg= "Red")
        messagebox.showerror ("Log in Panal" , "Blank box \n You are not allowed")
        my_button.config(bg= "lightblue")
    
    elif (username == "ayon") and (password == "12345"):
        my_button.config(bg= "green")
        messagebox.showinfo ("Log in Panal" , "Login successful \n You are allowed")
        my_button.config(bg= "lightblue")
    
    elif (username == "user") and (password == "user"):
        my_button.config(bg= "green")
        messagebox.showinfo ("Log in Panal" , "Login successful \n You are allowed")
        my_button.config(bg= "lightblue")

    elif (username == "python") and (password == "code1234"):
        my_button.config(bg= "green")
        messagebox.showinfo ("Log in Panal" , "Login succesful \n You are allowed")
        my_button.config(bg= "lightblue")
    
    else:
        my_button.config(bg= "Red")
        messagebox.showerror("Log in Panal" , "Login failed \n something is wrong \n Please try again")
        my_button.config(bg= "lightblue")


#creaing a button for log in
my_button = Button (root, text = "LOGIN" , font= ("Courier" , 20) , bg= "lightblue" , fg= "black" , borderwidth= 4, relief= RAISED ,command= login)
my_button.place (x= 160 , y = 200)


#it is the main loop of the program
root.mainloop()



