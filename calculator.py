from tkinter import*

print("CALCULATOR")

root = Tk()
root.geometry("1600x800+0+0")
root.title("CALCULATOR")
#====Variables and functions======
inputVar = StringVar()
clickOperator = " "
def cleanFunc():
    global clickOperator
    clickOperator = " "
    inputVar.set(" ")

def equalTo():
    global clickOperator
    equalsum = str(eval(clickOperator))
    inputVar.set(equalsum)
    clickOperator = " "

def clickBtn(click):
    global clickOperator
    clickOperator = clickOperator + str(click)
    inputVar.set(clickOperator)

#=========frames========
firstFrame = Frame(root, width=1600, height= 50, bg="saddlebrown", relief="sunken")
firstFrame.pack(side=TOP)
centFrame = Frame(root, width=500, height= 500, relief="solid")
centFrame.pack(side=LEFT)
secondFrame = Frame(root, width=800, height= 500, bg="saddlebrown", relief="solid")
secondFrame.pack(side=LEFT)
#=======BODY===========
headLabel = Label(firstFrame, font=("Verdana", 40, "bold"), text=("CALCULATOR"), fg="black", bd=20, anchor="w")
headLabel.grid(column=0, row=0)

inputBox = Entry(secondFrame, font=('Arial', 20), textvariable=inputVar, justify="right", bd=5, insertbackground="steel blue", insertwidth=4, bg= "aquamarine")
inputBox.grid(columnspan=5)

btnC = Button(secondFrame, command=cleanFunc, padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="C", bg='chocolate').grid(row=2, column=0)
btnSign = Button(secondFrame, command=lambda:clickBtn('-'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="+/-", bg='chocolate').grid(row=2, column=1)
btnPercent = Button(secondFrame, command=lambda:clickBtn('%'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="%", bg='chocolate').grid(row=2, column=2)
btnDiv = Button(secondFrame, command=lambda:clickBtn('/'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="/", bg='chocolate').grid(row=2, column=3)
btn7 = Button(secondFrame, command=lambda:clickBtn(7), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="7", bg='chocolate').grid(row=3, column=0)
btn8 = Button(secondFrame, command=lambda:clickBtn(8), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="8", bg='chocolate').grid(row=3, column=1)
btn9 = Button(secondFrame, command=lambda:clickBtn(9), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="9", bg='chocolate').grid(row=3, column=2)
btnX = Button(secondFrame, command=lambda:clickBtn('*'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="X", bg='chocolate').grid(row=3, column=3)
btn4 = Button(secondFrame, command=lambda:clickBtn(4), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="4", bg='chocolate').grid(row=4, column=0)
btn5 = Button(secondFrame, command=lambda:clickBtn(5), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="5", bg='chocolate').grid(row=4, column=1)
btn6 = Button(secondFrame, command=lambda:clickBtn(6), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="6", bg='chocolate').grid(row=4, column=2)
btnMinus = Button(secondFrame, command=lambda:clickBtn('-'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="-", bg='chocolate').grid(row=4, column=3)
btn1 = Button(secondFrame, command=lambda:clickBtn('1'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="1", bg='chocolate').grid(row=5, column=0)
btn2 = Button(secondFrame, command=lambda:clickBtn('2'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="2", bg='chocolate').grid(row=5, column=1)
btn3 = Button(secondFrame, command=lambda:clickBtn('3'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="3", bg='chocolate').grid(row=5, column=2)
btnPlus = Button(secondFrame, command=lambda:clickBtn('+'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="+", bg='chocolate').grid(row=5, column=3)
btn0 = Button(secondFrame, command=lambda:clickBtn('0'), padx=50, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="0", bg='chocolate').grid(row=6, columnspan=2)
btnPoint = Button(secondFrame, command=lambda:clickBtn('.'), padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text=".", bg='chocolate').grid(row=6, column=2)
btnEqual = Button(secondFrame, command=equalTo, padx=15, pady=15, bd=5, fg='black', font=('Arial', 17, 'bold'), text="=", bg='chocolate').grid(row=6, column=3)

root.mainloop()