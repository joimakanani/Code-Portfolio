# ****************************************************************************************************
#
#       Name:          Joi Wilson
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:    TicketCalculator.py
#       Due Date:      11/9/2020
#       Description:
#               Write a GUI program that calculates the price of a tickets dependent
#               on age and number of ticket
#
# ****************************************************************************************************

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x170')
var = IntVar()


class TicketCalculatorGui:
    def __init__(self):
        Radiobutton(root, text="Senior (<65)", variable=var, value=1).place(x=60, y=10)
        Radiobutton(root, text="Adult (15-65)", variable=var, value=2).place(x=60, y=40)
        Radiobutton(root, text="Child (5-15)", variable=var, value=3).place(x=60, y=70)
        label_1 = Label(root, text="Number of minutes for the call", font=("bold", 10))
        label_1.place(x=30, y=100)
        self.entry_1 = Entry(root, width="8")
        self.entry_1.place(x=220, y=100)
        Button(root, text='Display Charges', command=self.calculateCharges).place(x=60, y=130)
        Button(root, text='Quit', command=exitProgram).place(x=180, y=130)
        root.mainloop()

    def calculateCharges(self):
        charges = 0
        if var.get() == 1:
            numTix = float(self.entry_1.get())
            charges = numTix * 7.00
        if var.get() == 2:
            numTix = float(self.entry_1.get())
            charges = numTix * 12.00
        if var.get() == 3:
            numTix = float(self.entry_1.get())
            charges = numTix * 5.00
        messagebox.showinfo("Total Charges", "Your total charge = $" + str(round(charges, 2)))


def exitProgram():
    root.destroy()


if __name__ == '__main__':
    my_gui = TicketCalculatorGui()
