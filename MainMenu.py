from tkinter import *
from tkinter import messagebox

import APICredentialsManager
from APICredentialsWindow import APICredentialsWindow
from AnalysisWindow import AnalysisWindow
from ConfigureAxis import ConfigureAxis
from Axis import Axis

class MainMenu:
    def __init__(self):
        self.master = Tk()
        self.master.title("Twitter Analyser")
        self.root = Frame(self.master)

        menubar = Menu(self.master)
        menubar.add_command(label="API Tokens", command=lambda: APICredentialsWindow(self.master))
        self.master.config(menu=menubar)

        Label(self.master, text="Enter username").pack()
        self.username_entry = Entry(self.master)
        self.username_entry.insert(END, "@")
        self.username_entry.pack()

        Label(self.master, text="Number of tweets to use").pack()
        self.tweet_count_entry = Entry(self.master)
        self.tweet_count_entry.insert(END, "10")
        self.tweet_count_entry.pack()

        self.use_retweets = IntVar()
        Checkbutton(self.master, text='Use retweets?', variable=self.use_retweets, onvalue=1, offvalue=0).pack()

        self.axis = [Axis(0), Axis(1)]
        Button(self.master, text="Set up axis", command=lambda: ConfigureAxis(self)).pack(fill=BOTH)

        Button(self.master, text="Analyse", command=self.launch_analysis).pack(fill=BOTH)

        self.master.mainloop()

    def launch_analysis(self):
        if APICredentialsManager.get_credentials()[0] == "":
            messagebox.showerror("Error", "API Credentials not set")
            return
        if len(self.username_entry.get()) < 2:
            messagebox.showerror("Error", "Invalid username")
            return
        if self.username_entry.get()[0] != "@":
            messagebox.showerror("Error", "Invalid username (must begin with @)")
            return
        if not self.tweet_count_entry.get().isdigit():
            messagebox.showerror("Error", "Invalid number of tweets")
            return

        AnalysisWindow(self.master, self.axis, self.username_entry.get(), int(self.tweet_count_entry.get()), self.use_retweets.get() == 1)
