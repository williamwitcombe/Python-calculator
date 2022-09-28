# William Witcombe
#22/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import *
from turtle import color # import the tkinter library

def button_press(num):   # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():   # this block checks for the button_press(equals)
    
    global equation_text

    try:  # try is used in try...expect blocks. It defines a block of ode test if it contains any errors.
          # You can define different blocks for different errpr types, and blocks to execute if nothing went wrong.
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError: # Check for syntax error

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:   # Check for division by zero

        equation_label.set("arithmetic error")

        equation_text = ""

def clear(): # Clears the equation_label for the next calculation
    global equation_label
    global equation_text

    equation_label.set("")
    #equation_label.set= ""

    equation_text = str(" ") # Not removing the value
    equation_text = " "
    equation_label.set("")
    #equation_text = ""# Not removing the value

    #equation_text = (" ") # Not removing the value 
    #equation_text = " "# Not removing the value

    #equation_text = (" ")
    #equation_text = "" #not removing from the label
    #equation_text.set("") #giving exception
    

window = Tk()
window.title("Python Calculator")
window.geometry("550x600")
window.configure(bg="green")

equation_text = (" ")
equation_text = " "


equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 40), bg="blue", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

# create the buttons (0 - 9)

button1 = Button(frame, text=1, height=4, width=9, font=35, bg="purple", fg="orange" ,command=lambda: button_press(1))
button1.grid(row=2, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(2))
button2.grid(row=2, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(3))
button3.grid(row=2, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(7))
button7.grid(row=0, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(8))
button8.grid(row=0, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(9))
button9.grid(row=0, column=2)

button0 = Button(frame, text="0", height=4, width=9, font=35, bg="purple", fg="orange" , command=lambda: button_press(0))
button0.grid(row=3, column=1)

# create the operation buttons

plus = Button(frame, text='+', height=4, width=9, font=35, bg="red", command=lambda: button_press('+'))
plus.grid(row=3, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, bg="red", command=lambda: button_press('-'))
minus.grid(row=2, column=3)

multiply = Button(frame, text='X', height=4, width=9, font=35, bg="red", command=lambda: button_press('*'))
multiply.grid(row=1, column=3)

divide = Button(frame, text='÷', height=4, width=9, font=50, bg="red", command=lambda: button_press('/'))
divide.grid(row=0, column=3)

# create equals

equal = Button(frame, text='= ', height=4, width=9, font=35, command=equals, bg="red")
equal.grid(row=3, column=2)


# create clear button
#clear = Button (window, text='clear', height = 8, width=10, font=40, command=clear, bg = "red")
#clear.pack()

clears = Button (frame, text='Clear', height = 4, width=9, font=35, bg = "red", command=clear)
clears.grid(row=3,column=0)


window.mainloop()
