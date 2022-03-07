from tkinter import *
import APICredentialsManager


class APICredentialsWindow:
    def __init__(self, master):
        self.master = master
        self.top = Toplevel(master)
        self.top.grab_set()
        self.top.title("API Credentials")

        self.access_token, self.access_token_secret, \
            self.consumer_key, self.consumer_key_secret = APICredentialsManager.get_credentials()

        Label(self.top, text="Access Token").pack()
        self.access_token_entry = Entry(self.top)
        self.access_token_entry.insert(END, self.access_token)
        self.access_token_entry.pack()
        Label(self.top, text="Access Token Secret").pack()
        self.access_token_secret_entry = Entry(self.top)
        self.access_token_secret_entry.insert(END, self.access_token_secret)
        self.access_token_secret_entry.pack()
        Label(self.top, text="Consumer Key").pack()
        self.consumer_key_entry = Entry(self.top)
        self.consumer_key_entry.insert(END, self.consumer_key)
        self.consumer_key_entry.pack()
        Label(self.top, text="Consumer Key Secret").pack()
        self.consumer_key_secret_entry = Entry(self.top)
        self.consumer_key_secret_entry.insert(END, self.consumer_key_secret)
        self.consumer_key_secret_entry.pack()

        Button(self.top, text="Save", command=self.save).pack()

    def save(self):
        APICredentialsManager.save_credentials((
            self.access_token_entry.get(),
            self.access_token_secret_entry.get(),
            self.consumer_key_entry.get(),
            self.consumer_key_secret_entry.get()
        ))
        self.top.destroy()
