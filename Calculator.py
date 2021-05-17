from tkinter import *

root = Tk()
root.title("Satyam's Calculator")

e = Entry(root, width=65, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return


def clear():
    e.delete(0, END)


def button_add():
    first_Number = e.get()
    global f_number
    global math
    math = "add"
    f_number = float(first_Number)
    e.delete(0, END)


def button_back():
    a = e.get()
    word = a[:-1]
    e.delete(0, END)
    e.insert(0, word)


def button_percent():
    first_Number = e.get()
    global f_number
    global math
    math = "percent"
    f_number = float(first_Number)
    e.delete(0, END)


def button_divide():
    first_Number = e.get()
    global f_number
    global math
    math = "divide"
    f_number = float(first_Number)
    e.delete(0, END)


def button_multiply():
    first_Number = e.get()
    global f_number
    global math
    math = "product"
    f_number = float(first_Number)
    e.delete(0, END)


def button_subtract():
    first_Number = e.get()
    global f_number
    global math
    math = "minus"
    f_number = float(first_Number)
    e.delete(0, END)

def button_equal():
    secondNumber = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, f_number + float(secondNumber))
    if math == 'minus':
        e.insert(0, f_number - float(secondNumber))
    if math == 'product':
        e.insert(0, f_number * float(secondNumber))
    if math == 'divide':
        e.insert(0, f_number / float(secondNumber))
    if math == 'percent':
        e.insert(0, f_number / 100)


def button_transition():
    e.delete(0, END)
    e.insert(0, 'This Process does not work as of now')

def button_decimal():
    f_num = e.get()
    e.delete(0, END)
    e.insert(0, str(f_num) + '.')



button_AC = Button(root, text='AC', padx=35, pady=20, command=clear)
button_backspace = Button(root, text='⌫', padx=35, pady=20, command=button_back)
button_percent = Button(root, text='%', padx=38, pady=20, command=button_percent)
button_divide = Button(root, text='÷', padx=39, pady=20, command=button_divide)

button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_x = Button(root, text='x', padx=40, pady=20, command=button_multiply)

button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_minus = Button(root, text='-', padx=40.1, pady=20, command=button_subtract)

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_plus = Button(root, text='+', padx=39, pady=20, command=button_add)

button_transition = Button(root, text='➹', padx=37, pady=20, command=button_transition)
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_decimal = Button(root, text='.', padx=42, pady=20, command=button_decimal)
button_equal = Button(root, text='=', padx=39, pady=20, command=button_equal, fg='white', bg='orange')

button_AC.grid(row=1, column=0)
button_backspace.grid(row=1, column=1)
button_percent.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_x.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

button_transition.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_decimal.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()
