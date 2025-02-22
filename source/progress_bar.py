from time import time
from datetime import timedelta  # Human readable?
from tk import Tk
from tkinter import ttk


class progress_bar():
    """
    A Class meant to define all the relevant functions needed to make a
    functioning progress bar to display to the end user to give them an idea
    of how long it is going to take.
    """

    def __init__(self):
        """
        The initialization method for the progress_bar class we will be using.
        Main things of note are that it create the root node.
        Then makes a progress bar called pb that we can refer to later.

        :params class self: The class itself
        :returns: Nothing, modifies the class attributes.
        """

        self.root = Tk()
        self.root.geometry('500x120')
        self.root.title('Scraping Progress Bar')

        self.root.withdraw()

        # progress bar
        self.pb = ttk.Progressbar(
            self.root,
            orient='horizontal',
            mode='determinate',
            length=250,
            takefocus=True
        )

    def update_progress_label(self, CourseCode, start_time, lenn, i):
        """

        '''
        ======================
            TODO
        Author: rmathguy
        02-22-25 (M-D-Y)
        Finish this docstring
        '''

        :params class self: The class for the progressbar itself

        :params str CourseCode: The Course Code we are currently on and want
            to display

        :params int star_time: The time as an int (presumably?) since the
            Epoch started, gives us a reference point more or less.

        :returns: Nothing, modifies the class attributes.
        """

        time_ellapsed = time()-start_time

        if i == -1:
            timeleft = 0
        else:

            timeleft = (lenn / (i+1) - 1) * time_ellapsed

        outstr = (
                str(CourseCode) + " Successful \t " +
                f"{int(self.pb['value'])} % " + '\t Est. Time Left:' +
                str(timedelta(seconds=int(timeleft)))
                )

        return outstr

    def progress(self, CC, start_time, lenn, i, label):
        """

        :params class self: The class for the progressbar itself

        :params str CourseCode: The Course Code we are currently on and want
            to display

        :params int star_time: The time as an int (presumably?) since the
            Epoch started, gives us a reference point more or less.

        :returns: Nothing, modifies the class attributes.
        """
        if self.pb['value'] < 100:
            self.pb['value'] = (i+1) * 100 / lenn
            label['text'] = self.update_progress_label(CC, start_time, lenn, i)
            self.root.update()

    # place the progress bar
    def place(self, start_time, lenn):
        i = -1
        VL = ttk.Label(self.root,
                       text=self.update_progress_label("",
                                                       start_time, lenn, i))
        self.progress("", start_time, lenn, i, VL)
        self.pb.grid(column=0, row=0, columnspan=2, padx=150, pady=20)
