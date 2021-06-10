# ****************************************************************************************************
#
#       Name:          Joi Wilson
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:    FtoC.py
#       Due Date:      11/9/2020
#       Description:
#               Write a program that converts celsius to fahrenheit
#
# ****************************************************************************************************

import tkinter.messagebox
import tkinter


# ****************************************************************************************************

class CelsiusGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("converter")
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Celsius:')
        self.label2 = tkinter.Label(self.mid_frame, text='Fahrenheit:')
        self.entry1 = tkinter.Entry(self.top_frame, width=10)

        self.convert_button = tkinter.Button(self.top_frame,
                                             text='Convert to Fahrenheit',
                                             command=self.conFahr)
        self.convert_button2 = tkinter.Button(self.mid_frame,
                                              text='Convert to Celsius',
                                              command=self.conCel)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.value = tkinter.StringVar()

        self.result = tkinter.Entry(self.mid_frame, textvariable=self.value)
        self.result2 = tkinter.Entry(self.top_frame, textvariable=self.value)

        self.quit_button.pack(side='left')
        self.convert_button.pack(side='right')
        self.convert_button2.pack(side='right')
        self.label1.pack(side='left')
        self.entry1.pack(side='left')
        self.label2.pack(side='left')

        self.result.pack(side='left')
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    # ****************************************************************************************************

    def conFahr(self):
        fahrenheit = float(self.entry1.get())
        celsius = float((1.8 * fahrenheit) + 32)
        self.value.set(celsius)

    # ****************************************************************************************************

    def conCel(self):
        celsius = float(self.entry1.get())
        fahrenheit = float((celsius - 32) * 5 / 9)
        self.value.set(fahrenheit)


if __name__ == '__main__':
    my_gui = CelsiusGUI()
