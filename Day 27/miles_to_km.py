from tkinter import *

window = Tk()
window.title("Miles to Km Convertor")
window.config(padx=30, pady=30)
# window.minsize(width=500, height=300)

#Labels
m = Label(text="Miles")
m.grid(column=3, row=1)

iet = Label(text="is equal to")
iet.grid(column=1, row=2)

km = Label(text="0")
km.grid(column=2,row=2)

k = Label(text="Km")
k.grid(column=3, row=2)

#Entry
miles = Entry(width=10)
miles.grid(column=2, row=1)

def button_clicked():
    mi = float(miles.get())
    ki = 1.609 * mi
    km.config(text=str(ki))

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()