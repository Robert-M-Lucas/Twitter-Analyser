from tkinter import *

from matplotlib import pyplot as plt

import webbrowser

from Processor import Processor


class AnalysisWindow:
    def __init__(self, master, axis, username, tweet_count, use_retweets):
        self.axis = axis
        for a in self.axis:
            a.get_string()
        self.use_retweets = use_retweets
        self.username = username
        self.tweet_count = tweet_count
        self.processor = Processor(self)

        self.master = master
        self.top = Toplevel(master)
        self.top.grab_set()
        self.top.title("Analysis")

        self.root = None

        self.processing_text = StringVar()
        self.processing_text.set("Processing...")

        self.processing_view()
        self.start_processing()

    def processing_view(self):
        self.root = Frame(self.top)
        self.root.pack()

        Label(self.root, textvariable=self.processing_text).pack()

    def start_processing(self):
        self.processor.start()

    def processing_done(self):
        self.root.destroy()
        self.analysis_view()

    def analysis_view(self):
        print("Done")
        self.root = Frame(self.top)
        self.root.pack()

        Label(self.root, text="Analysis: " + self.username).pack()

        Label(self.root, text="X Axis: " + self.axis[0].string).pack()
        Label(self.root, text="Y Axis: " + self.axis[1].string).pack()

        Button(self.root, text="Show Graph", command=self.show_graph).pack(fill=BOTH)

    def on_pick(self, event):
        print(self.processor.df['is_retweet'][event.ind[0]])
        webbrowser.open(f"https://twitter.com/none/status/{self.processor.df['id'][event.ind[0]]}")

    def show_graph(self):
        # time_likes = pd.Series(data=self.processor.df['likes'].values, index=self.processor.df['len'])
        # time_likes.plot(figsize=(16, 4), label="Retweets/Likes", legend=False)

        ax = self.processor.df.plot.scatter(x='x', y='y', c='DarkBlue', picker=10)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        plt.xlabel(self.axis[0].string)
        plt.ylabel(self.axis[1].string)

        # time_likes = pd.Series(data=self.processor.df['likes'].values, index=self.processor.df['date'])
        # ax = time_likes.plot(style=".", figsize=(16, 4), label="Retweets/Likes", legend=False)

        fig = ax.get_figure()

        plt.title(self.username)

        fig.set_figheight(4)

        plt.subplots_adjust(bottom=0.25)

        fig.canvas.callbacks.connect('pick_event', self.on_pick)
        plt.show()

