#graphical user interface
import tkinter as tk

def greet():
    label.config(text="Hello, Welcome to Nepal")

root =tk.Tk()

root.title("My First App")

root.geometry("500x300")

label =tk.Label(root,text="Hello Nepal!")

#add button
button=tk.Button(root,text="Greet me",command=greet)
button.pack(pady=10)

label.pack()

root.mainloop()