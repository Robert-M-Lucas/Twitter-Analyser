from tkinter import *
from tkinter import messagebox

from Axis import Axis
import Operations as op
from OperationSelector import OperationSelector

class ConfigureAxis:
    def __init__(self, MainMenu):
        self.master = MainMenu.master
        self.MainMenu = MainMenu
        self.top = Toplevel(self.master)
        self.top.grab_set()
        self.top.title("Configure Axis")
        self.axis = 0

        self.axis_var = StringVar(self.master)
        self.axis_var.set("Axis 1")  # default value

        OptionMenu(self.top, self.axis_var, "Axis 1", "Axis 2").pack(fill=BOTH)
        self.axis_var.trace("w", self.change_axis)

        self.starting_value_var = StringVar()
        self.operation_listbox = StringVar()

        self.root = None
        self.render_axis()

    def change_axis(self, *args):
        self.axis = int(self.axis_var.get()[-1]) - 1
        self.render_axis()

    def render_axis(self):
        if self.root is not None:   self.root.destroy()

        self.root = Frame(self.top)
        self.root.pack()

        if self.axis == 0:  text = "X Axis"
        else:   text = "Y Axis"

        Label(self.root, text=text).pack()
        Label(self.root, text="Starting value").pack()

        self.starting_value_var.set(self.get_current_axis().starting_value)
        OptionMenu(self.root, self.starting_value_var, *op.Values.keys()).pack(fill=BOTH)
        self.starting_value_var.trace("w", self.change_starting_value)

        self.operation_listbox.set(value=self.get_current_axis().operations)
        Listbox(self.root, height=10, listvariable=self.operation_listbox).pack()

        Button(self.root, text="Delete Operation", command=self.delete_operation).pack(fill=BOTH)
        Button(self.root, text="Add Operation", command=self.add_operation).pack(fill=BOTH)

        btn_txt = StringVar()
        btn_txt.set("Save")
        Button(self.root, textvariable=btn_txt, command=lambda: self.save_axis(btn_txt)).pack(fill=BOTH)

    def delete_operation(self):
        self.update_operations(self.MainMenu.axis[self.axis].operations[:-2])

    def add_operation(self):
        if op.Values[self.starting_value_var.get()][1]:
            OperationSelector(self)
        else:
            messagebox.showerror("Error", f"This starting value ({self.starting_value_var.get()}) doesn't support operations")

    def change_starting_value(self, *args):
        if not op.Values[self.starting_value_var.get()][1]:
            self.update_operations([])

    def update_operations(self, new_operations):
        self.MainMenu.axis[self.axis].operations = new_operations
        self.operation_listbox.set(value=self.MainMenu.axis[self.axis].operations)

    def get_current_axis(self):
        return self.MainMenu.axis[self.axis]

    def save_axis(self, btn_text):
        self.MainMenu.axis[self.axis].starting_value = self.starting_value_var.get()

        self.MainMenu.axis[self.axis].save()
        btn_text.set("Saved!")
        self.root.after(2000, lambda: btn_text.set("Save"))

