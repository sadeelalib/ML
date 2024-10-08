import tkinter as tk


def load_frame2():
    print("Hello World")

parent = tk.Tk()
parent.geometry("400x300")
parent.title("Login Form")
parent.eval("tk::PlaceWindow . center")
name = tk.Label(parent, text = "Name").place(x = 30, y = 50)
email = tk.Label(parent, text = "User ID").place(x = 30, y = 90)
password =  tk.Label(parent, text = "Password").place(x = 30, y = 130)
tk.Button(parent, text="Submit", activebackground="green", activeforeground="blue",
          command=lambda:load_frame2()).place(x=120, y=170)
entry1 = tk.Entry(parent).place(x = 85, y = 50)
entry2 = tk.Entry(parent).place(x = 85, y = 90)
entry3 = tk.Entry(parent).place(x = 90, y = 130)
parent.mainloop()
