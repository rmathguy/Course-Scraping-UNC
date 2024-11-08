# %% Imports{{{
'''Only needed if you want to measure how long it takes'''
from time import time  # timing purposes only
from time import sleep
# above makes sure it doesn't get kicked for accessing the site too much

# CUSTOM CODE IMPORTS
import Page_Search_Excel_Add
import EXCEL_START_FUNC
import Webpage_and_Driver_Start

# For extra windows.
from tkinter import ttk
import tkinter as tk
from sys import exit
from csv_reader import read_csv

# For saving file location.
import easygui

# }}}


# %% Main {{{
def main(COURSE_LIST, EmailVar):

    save_name = easygui.filesavebox(default="save.xlsx", filetypes=["*.xlsx"])

    if save_name is None:
        easygui.exceptionbox("You must choose a save file name", "Note")
        save_name = easygui.filesavebox(default="save.xlsx", filetypes=["*.xlsx"])
        if save_name is None:
            exit()

    start_time = time()
    lenn = len(COURSE_LIST)  # To give an idea of how far we are later

    root = tk.Tk()
    root.geometry('500x120')
    root.title('Scraping Progress Bar')

    root.withdraw()

    def update_progress_label(CC, start_time, lenn, i):
        time_ellapsed = time()-start_time
        if i == -1:
            timeleft = 0
        else:
            timeleft = (lenn / (i+1) - 1) * time_ellapsed
        return (str(CC) + " Successful \t " + f"{int(pb['value'])} % " +
                '\t Est. Time Left:'+str(int(timeleft))+'s')

    def progress(CC, start_time, lenn, i, label):
        if pb['value'] < 100:
            pb['value'] = (i+1) * 100 / lenn
            label['text'] = update_progress_label(CC, start_time, lenn, i)
        root.update()        

    # progress bar
    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=250,
        takefocus=True
    )
    # place the progress bar
    i = -1
    VL = ttk.Label(root, text=update_progress_label("", start_time, lenn, i))
    progress("", start_time, lenn, i, VL)
    pb.grid(column=0, row=0, columnspan=2, padx=150, pady=20)

    # Excel Stuff {{{

    (Excel_info, Cells) = EXCEL_START_FUNC.ESF()
    WS = Excel_info[1]
    WB = Excel_info[0]

    # }}}

    # Driver {{{
    driver = Webpage_and_Driver_Start.main(EmailVar)  # }}}

    #  Iterate on the Courses:# {{{
    '''Loop over the Function'''
    for i, CC in enumerate(COURSE_LIST):
        value_label = ttk.Label(root, text=update_progress_label(CC, start_time, lenn, i))
        value_label.grid(column=0, row=1, columnspan=2)
        sleep(1)
        try:
            Page_Search_Excel_Add.main(CC, driver, WS, Cells, EmailVar)
            progress(CC, start_time, lenn, i, value_label)
        except Exception:
            try:
                sleep(5)
                Page_Search_Excel_Add.main(CC, driver, WS, Cells, EmailVar)
                progress(CC, start_time, lenn, i, value_label)
            except Exception:
                sleep(10)
                Page_Search_Excel_Add.main(CC, driver, WS, Cells, EmailVar)
                progress(CC, start_time, lenn, i, value_label)
        if i == 0:
            root.deiconify()
            root.update()
    # Close the Webpage {{{
    driver[0].quit()  # }}}

    # SAVES THE DATA TO AN EXCEL FILE{{{
    '''ONLY USE BELOW WHEN READY'''

    WB.save(save_name)  # }}}

    # Runtime Info{{{

    # }}}
# }}}
