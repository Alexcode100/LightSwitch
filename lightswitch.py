#Alexander den Otter - 99067410
import tkinter as tk
window = tk.Tk()
window.geometry('300x300')

# schijf hier tussen je code
waarde = True
def LichtSchakelaar():
    global waarde
    if waarde:
        print('light on')
        Knop.configure(text="turn off")
        window.configure(bg="yellow")
        waarde = False
    else:   
        print('light off')
        Knop.configure(text="turn on")
        window.configure(bg="black")
        waarde = True

Knop = tk.Button(text = 'Click to turn on',bg = 'white', fg = 'black', command = LichtSchakelaar)

Knop.pack()
Knop.place(relx=0.5, rely=0.5, anchor='center')
# schijf hier tussen je code

window.mainloop()