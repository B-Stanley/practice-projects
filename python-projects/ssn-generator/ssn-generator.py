from tkinter import *
import random
import sqlite3
import tkinter.messagebox as tmb
#from PIL import Image, ImageTk


win = Tk()
#add a title
win.title("SSN GENERATOR 1.0")
win.geometry("750x500")
#functions

firstname = StringVar()
lastname = StringVar()
dob = StringVar()
city = StringVar()
postcode = StringVar()
email = StringVar()
height = StringVar()
age = StringVar()
var1 = IntVar()
rs = StringVar()
social = random.randrange(0,1000000000)
display = Entry(win)

def phrase_display():
    global social
    global display
         #this creates the text field
    tmb.showinfo('Your SSN Number', message= '%s %s' %('This is your social security number: ', social))
    display = Entry(win)
    display.place(x= 180, y= 500)
    display.insert(END, social)
    return
def database():
    global social
    Fname = firstname.get()
    Lname = lastname.get()
    DOB = dob.get()
    City = city.get()
    Postcode = postcode.get()
    State = rs.get()
    Email = email.get()
    Height = height.get()
    Age = age.get()
    Gender = var1.get()
    SSN = display.get()

    conn = sqlite3.connect('ssn.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Applicant (FNAME TEXT, LNAME TEXT, DOB TEXT, CITY TEXT, POSTCODE TEXT, STATE TEXT, EMAIL TEXT, HEIGHT TEXT, AGE TEXT, GENDER TEXT, SSN INTEGER)')
    cursor.execute('INSERT INTO Applicant (FName, Lname, DOB, City, Postcode, State, Email, Height, Age, Gender, SSN) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                   (Fname, Lname, DOB, City, Postcode, State, Email, Height, Age, Gender, SSN))
    conn.commit()

#label

tops = Frame(win, width=100,height = 50 ,bg="black", relief=SUNKEN)
tops.pack(side=TOP)

bottom = Frame(win, width = 1200, height = 800)
bottom.pack(side=TOP)

#background_image1 = PhotoImage(file='C:\\Users\\NENE\\Desktop\\SSN.png')
#background_label1 = Label(tops, image=background_image1)
#background_label1.pack(side=LEFT)
#background_label1.place(x=0, y=0, relwidth=1, relheight=1)

#backimage = Canvas(win, bg='blue', height= 700, width= 1000)
#background_image = PhotoImage(file='C:\\Users\\NENE\\Desktop\\SSN bg.png')
#background_label = Label(bottom, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#backimage.pack()

label0= Label(tops, text= 'SSN GENERATOR', width = 50, font=("Century", 40, "bold"), fg = 'White', bg= 'black')
label0.pack()

label1=Label(bottom,text= "Firstname", width = 15, font=('century', 10, 'italic'),bg = 'darkolivegreen2')
label1.place(x=80, y=120)
entry1 = Entry(bottom, textvar=firstname, width= 40)
entry1.place(x=220, y=120)

label2= Label(bottom,text= "Lastname", width = 15, font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label2.place(x=80, y=150)
entry2 = Entry(bottom, textvar=lastname, width= 40)
entry2.place(x=220, y=150)

label1=Label(bottom,text= "Email", width = 15, font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label1.place(x=80, y=175)
entry1 = Entry(bottom, textvar=email, width= 40)
entry1.place(x=220, y=175)


label3= Label(bottom,text= "Date of Birth",width=15,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label3.place(x=80, y=200)

label3= Label(bottom,text= "Day",width=8,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label3.place(x=220, y=200)
spin = Spinbox(bottom, from_=0, to=31, width=5, textvariable = dob)
spin.place(x=300, y=200)

label3= Label(bottom,text= "Month",width=8,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label3.place(x=350, y=200)
spin = Spinbox(bottom, from_=1, to=12, width=5)
spin.place(x=430, y=200)

label3= Label(bottom,text= "Year",width=8,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label3.place(x=480, y=200)
spin = Spinbox(bottom, from_=1960, to=2009, width=5)
spin.place(x=560, y=200)

label4= Label(bottom,text= "City",width=15,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label4.place(x=80, y=225)
entry4 = Entry(bottom, textvar=city, width= 40)
entry4.place(x=220, y=225)

label4= Label(bottom,text= "Postcode",width=15,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label4.place(x=80, y=250)
entry4 = Entry(bottom, textvar=postcode, width= 40)
entry4.place(x=220, y=250)
label4= Label(bottom,text= "State",width=15,font=('century', 10, 'italic'), bg = 'darkolivegreen2')
label4.place(x=80, y=275)
statelist = ['Abia', 'Adamawa', 'Akwa-Ibom', 'Anambara', 'Bauchi', 'Benue', 'Cross-River', 'Delta', 'Edo', 'Ekiti', 'Imo'];

droplist = OptionMenu(bottom, rs, *statelist)
droplist.config(width=30, bg = 'darkolivegreen2')
rs.set('Resident state')
droplist.place(x=220, y=275)

radiobutton = Radiobutton(bottom, font=('century', 10, 'italic'), text="male",padx=5, variable = var1, value=1).place(x=220, y=320)
radiobutton1 = Radiobutton(bottom, font=('century', 10, 'italic'), text="female",padx=15, variable = var1, value=2).place(x=280, y=320)

label4 = Label(bottom,text= "Height",width=15,font=('century',10, 'italic'),bg = 'darkolivegreen2')
label4.place(x=80, y=350)
entry4 = Entry(bottom, textvar=height, width= 40)
entry4.place(x=220, y=350)
label5= Label(bottom,text= "Age",width=15,font=('century', 10, 'italic'),bg = 'darkolivegreen2')
label5.place(x=80, y=375)
entry5 = Entry(bottom, textvar=age, width= 40)
entry5.place(x=220, y=375)

button1 = Button(bottom, font=('century', 10, 'italic'), text= "GET SSN", bg="brown3", command=phrase_display)
button1.place(x=200, y=400)


button2 = Button(bottom, font=('century', 10, 'italic'), text= "SUBMIT", bg = 'chartreuse4' , command=database)
button2.place(x=200, y=450)

win.mainloop()
