#In this project I am making a cipher code encryption and decrypption

#importing tkinter for GUI
from tkinter import *

#importing string for code
import string
#importing filedialog
from tkinter import filedialog

#making the display
root = Tk()
root.title("Cipher code encryption and Decryption GUI made by Ayon Saha")
root.geometry("600x600")





#background change
root.config (bg= "lightblue")



#defining button click for encryption key
def button_click1():
    global shift
    num= key_button1.get()
    #shifting key selection
    shift = 26 - int(num)
    shift %= 26

#defining function for encrypt
def encrypt():
    global shift
    #taking the text
    plain_text = encryption.get(1.0,END)

    #making encryption
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet , shifted)

    encrypted= plain_text.translate(table)

    #opening filedialouge for saving encrypted file
    open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
    if open_file is None:
        return
    text= str(encrypted)
    open_file.write(text)
    open_file.close()


#defining text label 1
my_label1 = Label (root , text= "Paste your text for encryption" ,font= ("Helvetica" , 8) )
my_label1.place (x= 50 , y= 10)

#taking text for encryption
encryption =Text(root , width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
encryption.place(x= 50 , y= 30)



#defining text label 2
my_label2 = Label (root,text= "Select your encryption key:" ,font=("Helveica" , 8) )
my_label2.place (x= 60 , y= 130)

#creating button for  encryption Key
key_button1 = Spinbox(root ,from_= 1,to= 26, font= ("courier" , 10) ,  command= button_click1)
key_button1.place (x=200 , y= 130)



#making a button for encryption
en_button = Button (root ,width= "15" , height= "5" ,text= "Encryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= encrypt)
en_button.place (x=400 , y= 130)


'''
====================================================================================================================
'''
#defining button click for decryption key
def button_click2():
    global shift
    num1 = key_button2.get()
    #shifting key selection
    shift = 26 + int(num1)
    shift %= 26


#defining function for decrypt
def decrypt():
    global shift
    #taking the text
    plain_text = decryption.get(1.0,END)

    #making decryption
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet , shifted)

    decrypted= plain_text.translate(table)

    #opening filedialouge for saving decrypted file
    open_file= filedialog.asksaveasfile(mode= "w" , defaultextension= ".txt")
    if open_file is None:
        return
    text= str(decrypted)
    open_file.write(text)
    open_file.close()


#defining text label 3
my_label3 = Label (root , text= "Paste your text for decryption" ,font= ("Helvetica" , 8) )
my_label3.place (x= 50 , y= 280)

#taking text for decryption
decryption =Text(root , width= "60" , height= "5" , wrap= WORD , borderwidth= 6)
decryption.place(x= 50 , y= 300)




#defining text label 4
my_label4 = Label (root,text= "Select your decryption key:" ,font=("Helveica" , 8) )
my_label4.place (x= 60 , y= 400)

#creating button for  decryption Key
key_button2 = Spinbox(root ,from_=1,to=26 , font= ("courier" , 10) ,  command=button_click2)
key_button2.place (x=200 , y= 400)


#making a button for decryption
en_button = Button (root ,width= "15" , height= "5" , text= "Decryption" , font= ("courier" , 9) ,borderwidth=2,relief=RIDGE,command= decrypt)
en_button.place (x=400 , y= 400)



#defining text label 5
my_label5 =Label (root,text= "  Chipper Code Encryption And Decryption  " ,font=("Helveica" , 11),borderwidth=4,relief=GROOVE )
my_label5.place (x= 150 , y= 520 )




#it is the mainloop of the proggram
root.mainloop()



