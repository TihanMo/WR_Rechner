# Author: Ael Banyard

from tkinter import *

# Config of Window
root = Tk(className=" WR - Ael Banyard / Tihan Morrol")
root.geometry("500x800")
title = StringVar()
label = Label(root, textvariable=title, font=10)
title.set("WR Rechner für Renditen")

# Set Vars
ek = [90, 80, 70, 60, 50, 40, 30, 20, 10]
roi = 0.12

# Create Table
def table(fkzins):
    test = Frame(root, relief="groove", bd=1)

    Label(test, text="Bei einem Fremdkapitalzins von: " + str(fkzins*100) + "%", font=6).grid(row=0, columnspan=4, sticky="w")
    Label(test, text="Eigenkapital", font=4).grid(column=0, row=1, sticky="w")
    Label(test, text="Fremdkapital", font=4).grid(column=1, row=1, sticky="w")
    Label(test, text="Gewinn", font=4).grid(column=2, row=1, sticky="w")
    Label(test, text="RoE", font=4).grid(column=3, row=1, sticky="w")

    for x in range(9):
        fk = 100-ek[x]
        gewinn = (roi*100)-(fk*fkzins)
        roe = (gewinn/ek[x]) * 100
        Label(test, text=ek[x]).grid(column=0, row=x+2, sticky="w")
        Label(test, text=fk).grid(column=1, row=x+2, sticky="w")
        Label(test, text=gewinn).grid(column=2, row=x+2, sticky="w")
        Label(test, text=str(roe) + "%").grid(column=3, row=x+2, sticky="w")
    test.pack()



# Render of Window
label.pack()
table(0.05)
table(0.1)
table(0.15)
root.mainloop()

