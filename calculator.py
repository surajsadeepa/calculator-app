from tkinter import *


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set('syntax error')

        equation_text = ''

    except ZeroDivisionError:

        equation_label.set('arithmetic error')

        equation_text = ''


def clear():

    global equation_text

    equation_label.set('')

    equation_text = ''


window = Tk()
window.title('Calculator program')
window.config(bg='black')
window.resizable(False, False)

equation_text = ''

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20), bg='black',
              width=24, height=2, fg='white')
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1), bg='black', fg='white', activebackground='black', activeforeground='white')
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2), bg='black', fg='white', activebackground='black', activeforeground='white')
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3), bg='black', fg='white', activebackground='black', activeforeground='white')
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4), bg='black', fg='white', activebackground='black', activeforeground='white')
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5), bg='black', fg='white', activebackground='black', activeforeground='white')
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6), bg='black', fg='white', activebackground='black', activeforeground='white')
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7), bg='black', fg='white', activebackground='black', activeforeground='white')
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8), bg='black', fg='white', activebackground='black', activeforeground='white')
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9), bg='black', fg='white', activebackground='black', activeforeground='white')
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0), bg='black', fg='white', activebackground='black', activeforeground='white')
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
              command=lambda: button_press('+'), bg='#FF9500', fg='white', activebackground='#FF9500', activeforeground='white')
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
               command=lambda: button_press('-'), bg='#FF9500', fg='white', activebackground='#FF9500', activeforeground='white')
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                  command=lambda: button_press('*'), bg='#FF9500', fg='white', activebackground='#FF9500', activeforeground='white')
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                command=lambda: button_press('/'), bg='#FF9500', fg='white', activebackground='#FF9500', activeforeground='white')
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
               command=equals, bg='black', fg='white', activebackground='black', activeforeground='white')
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'), bg='black', fg='white', activebackground='black', activeforeground='white')
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=39, font=35,
               command=clear, bg='#333333', fg='white', activebackground='#333333', activeforeground='white')
clear.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))


window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
