import tkinter as tk

window = tk.Tk()
window.title('bilibili download')
window.geometry('680x400')
# window.resizable(False, False)

mylabel = tk.Label(window, text='Down Url:')
mylabel.grid(row=0, column=0)
myentry = tk.Entry(window)
myentry.grid(row=0, column=1)




test = tk.Button(text="測試")
# test.pack(side="top")
# window.iconbitmap('icon.ico')
window.mainloop()

