import tkinter as tk

window = tk.Tk()
window.geometry("300x200")

gender = tk.StringVar()

male = tk.Radiobutton(window, text="Male", variable=gender, value="Male")
male.pack()

female = tk.Radiobutton(window, text="Female", variable=gender, value="Female")
female.pack()

window.mainloop()