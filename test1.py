
import tkinter as tk

root = tk.Tk()
root.title('my window')

mylabel = tk.Label(root, text='Name:')
mylabel.grid(row=0, column=0)
myentry = tk.Entry(root)
myentry.grid(row=0, column=1)

root.mainloop()