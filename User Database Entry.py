# importing the module
from  tkinter import *
import  datetime


# date of userid and pass into the databasse
a=datetime.datetime.now()

# initializing the GUI
root=Tk()
root.geometry("500x500")

#  Headline
headLine=Label(root,text="Dopekid Corpration LMT.", font="airstrike 22 ",bg="black",fg="white")
headLine.pack(fill=X)

# asking for username and password
lable=Label(root,text="Enter your Username and Password",font='highspeed 10 italic',bg="black",fg="white")
lable.pack(fill=X,)

# username for showing
username=Label(root,text="Username",font='dream 10 italic',bg="white",fg="black")
password=Label(root,text="Password",font="dream 10 italic",bg="white",fg='black',padx=2)

# packing username and passwrod as grid
username.pack(side=TOP,anchor="w")
password.pack(side=TOP,anchor="w")

# entry for username and password
uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue,bg="grey")
passentry=Entry(root,textvariable=passvalue,bg="grey")

#       placing the entry
userentry.place(x=80,y=56)
passentry.place(x=80,y=78)

#  Submit
def submit():
    print("Your Data Has Been Recorded Successfully...")
    with open("dopekid Corp.txt",'w') as f:
        f.writelines(f"id=['{userentry.get()}','{passentry.get()}']")

#  Placing button
b1 = Button(root,text="Submit",font="elephant 9 italic",command=submit,bg="grey",fg="black",borderwidth=3)
b1.place(x=220,y=65)



# Adding the background
img=PhotoImage(file='hello.png')
photo=Label( image=img)
photo.pack()


root.mainloop()

