from tkinter import *
from tkinter import messagebox

from Axis import Axis
import Operations as op


class OperationSelector:
    def __init__(self, configureAxis):
        self.master = configureAxis.master
        self.ConfigureAxis = configureAxis
        self.top = Toplevel(self.master)
        self.top.grab_set()
        self.top.title("Select operation")

        Label(self.top, text="Select an operation").pack()
        self.operation_var = StringVar(self.master)
        self.operation_var.set(list(op.Operations.keys())[0])

        OptionMenu(self.top, self.operation_var, *list(op.Operations.keys())).pack()

        Label(self.top, text="Select a value").pack()
        self.value_var = StringVar()
        self.value_var.set("Constant")
        OptionMenu(self.top, self.value_var, *["Constant"] + list(op.Values.keys())).pack()
        self.value_var.trace("w", self.change_value)

        self.value_entry = Entry(self.top)
        self.value_entry.pack()

        Button(self.top, text="Add", command=self.done).pack()

    def change_value(self, *args):
        if self.value_var.get() != "Constant":
            self.value_entry.config(state=DISABLED)
        else:
            self.value_entry.config(state=NORMAL)

    def done(self):
        value = None
        if self.value_var.get() == "Constant":
            try:
                value = float(self.value_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Value must be a float")
                return
        else:
            value = self.value_var.get()
        self.ConfigureAxis.update_operations(self.ConfigureAxis.get_current_axis().operations + [self.operation_var.get(), str(value)])

        self.top.destroy()
