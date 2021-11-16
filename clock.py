from tkinter import *
import time
#root is our main display 
root = Tk()
root.title("Clock made by Ayon Saha")
root.geometry("600x350")

#defining clock function
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm= time.strftime("%p")
    day = time.strftime("%A")
    week = time.strftime("%w")
    month = time.strftime("%B")
    year = time.strftime("%Y")
    

    my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm )
    my_label.after(1000 , clock)
    my_label_day.config(text= day + " : " + week + " no of week this Month   ")
    my_label_mounth.config(text= month)
    my_label_year.config(text= year)


#creating label for hour,min,second
my_label= Label (root , text= " " , font= ("Helvetica" , 60), fg= "cyan", bg= "black")
my_label.pack(padx=20)


#creating label for day
my_label_day = Label(root , text  = " " ,font= ("Helvetica" , 20),border=8, relief= GROOVE)
my_label_day.pack(padx=10)


#creating label for mounth
my_label_mounth = Label(root , text  = " " ,font= ("Helvetica" , 30) ,border=8,relief= GROOVE)
my_label_mounth.pack(padx=10)

#creating label for year
my_label_year = Label(root , text  = " " ,font= ("Helvetica" , 25),border=8, relief= GROOVE)
my_label_year.pack(padx=10)



#creating zone function
def zone():
    timezone=time.strftime("%Z")
    my_timezone_show = Label(root , text= timezone , font= ("Helvetica" , 14))
    my_timezone_show.pack(padx=10)

    
 
#creating a button to show timezone
my_button_timezone = Button(root , text= " show time zone" ,border=3, relief= RIDGE, command= zone )
my_button_timezone.pack(padx=10)
#calling clock function
clock()



#it is the mainloop of the proggram
root.mainloop()
