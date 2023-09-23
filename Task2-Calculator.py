from tkinter import *

def btn_click(number):
    current = input_text.get()
    input_text.set(current + str(number))

def btn_clear():
    input_text.set("")

def calculate():
    try:
        result = eval(input_text.get())
        input_text.set(str(result))
    except:
        input_text.set("Error")

root = Tk()
root.title("Simple Calculator")
root.geometry("312x330")
root.resizable(0, 0)

input_text = StringVar()
input_frame = Frame(root, width=312, height=50, highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="light blue", bd=5)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame, text="C", fg="white", width=32, height=3, bd=0, bg="black", cursor="hand2", command=btn_clear)
clear.grid(row=0, column=0, columnspan=3, padx=2, pady=2)

divide = Button(btns_frame, text="/", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
                command=lambda: btn_click("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

seven = Button(btns_frame, text="7", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
               command=lambda: btn_click(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
               command=lambda: btn_click(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
              command=lambda: btn_click(9))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
                  command=lambda: btn_click("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

four = Button(btns_frame, text="4", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
              command=lambda: btn_click(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
              command=lambda: btn_click(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
             command=lambda: btn_click(6))
six.grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
               command=lambda: btn_click("-"))
minus.grid(row=2, column=3, padx=1, pady=1)

one = Button(btns_frame, text="1", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
             command=lambda: btn_click(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
             command=lambda: btn_click(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
               command=lambda: btn_click(3))
three.grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
              command=lambda: btn_click("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

zero = Button(btns_frame, text="0", fg="white", width=21, height=3, bd=0, bg="black", cursor="hand2",
              command=lambda: btn_click(0))
zero.grid(row=4, columnspan=2, column=0, padx=1, pady=1)

decimal = Button(btns_frame, text=".", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
                 command=lambda: btn_click("."))
decimal.grid(row=4, column=2, padx=1, pady=1)

equal = Button(btns_frame, text="=", fg="white", width=10, height=3, bd=0, bg="black", cursor="hand2",
               command=calculate)
equal.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
