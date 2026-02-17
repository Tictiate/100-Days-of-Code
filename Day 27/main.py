import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# label.pack() #Loads it on
label["text"] = "New Text"
label.config(text="New Text")
label.grid(column=1, row=1)

def button_clicked():
    new_text = input.get()
    label["text"] = f"{new_text}"

#Button
button = tkinter.Button(text="Click Me", command= button_clicked)
button.grid(column=2, row=2)
# button.pack()

#Entry
input = tkinter.Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=4, row=3)

new_button = tkinter.Button(text="Joe")
new_button.grid(column=3, row=1)



window.mainloop()