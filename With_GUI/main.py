# Author: Ael Banyard
import tkinter
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Config of Window
root = Tk(className=" WR - Ael & Tihan")
title = StringVar()
label = Label(root, textvariable=title, font=10)
title.set("WR Rechner für Renditen")


# Set Vars
ek = [90, 80, 70, 60, 50, 40, 30, 20, 10]
roi = 0.12
roe5 = []
roe10 = []
roe15 = []
# Create Table
def table(fkzins, c):
    test = Frame(root, relief="groove", bd=1)

    Label(test, text="Bei einem Fremdkapitalzins von: " + str(fkzins*100) + "%", font=6).grid(row=0, columnspan=4, sticky="w")
    Label(test, text="Eigenkapital", font=4).grid(column=0, row=1, sticky="w")
    Label(test, text="Fremdkapital", font=4).grid(column=1, row=1, sticky="w")
    Label(test, text="Gewinn", font=4).grid(column=2, row=1, sticky="w")
    Label(test, text="RoE", font=4).grid(column=3, row=1, sticky="w")

    roeAr = []
    for x in range(9):
        fk = 100-ek[x]
        gewinn = (roi*100)-(fk*fkzins)
        roeAr.append((gewinn/ek[x]) * 100)
        roe = (gewinn/ek[x]) * 100
        Label(test, text=ek[x]).grid(column=0, row=x+2, sticky="w")
        Label(test, text=fk).grid(column=1, row=x+2, sticky="w")
        Label(test, text=gewinn).grid(column=2, row=x+2, sticky="w")
        Label(test, text=str(roe) + "%").grid(column=3, row=x+2, sticky="w")
    test.grid(column=c, row=1)
    return roeAr



# Render of Window
label.grid(column=0, row=0, columnspan=3)
roe5 = table(0.05, 0)
roe10 = table(0.1, 1)
roe15 = table(0.15, 2)

nr = [1,2,3,4,5,6,7,8,9]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(nr, ek, edgecolor="blue", color="white")
plt.plot(nr, roe5, color="green", label="5% FK-Zins")
plt.plot(nr, roe10, color="blue", label="10% FK-Zins")
plt.plot(nr, roe15, color="red", label="15% FK-Zins")
plt.legend(loc="upper center")

scatter = FigureCanvasTkAgg(fig, root)
scatter.get_tk_widget().grid(column=0, row=2, columnspan=3)


root.mainloop()

