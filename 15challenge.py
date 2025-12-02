#GUI for Simple interest
#graphical user interface
import tkinter as tk
from tkinter import messagebox

def simple_interest():
    P=entry1.get()
    R=entry2.get()
    T=entry3.get()
    if P.isdigit() and R.isdigit() and T.isdigit():
        mul=float(P)*float(R)*float(T)
        Simple_Interst=mul/100
        messagebox.showinfo("Result",f"Simple Interest: {Simple_Interst}")
    else:
        messagebox.showerror("Error", "Enter Valid numbers")

root =tk.Tk()
root.title("Simple Interest App")

#input fields
label1=tk.Label(root,text="P:Principal amount")
entry1=tk.Entry(root)
label1.pack(pady=5)
entry1.pack(pady=5)
label2=tk.Label(root,text="R:Rate of iinterest")
entry2=tk.Entry(root)
label2.pack(pady=5)
entry2.pack(pady=5)
label3=tk.Label(root,text="T:Time period")
entry3=tk.Entry(root)
label3.pack(pady=5)
entry3.pack(pady=5)

root.geometry("500x500")

button=tk.Button(root,text="Simple Interest",command=simple_interest)
button.pack(pady=10)



root.mainloop()