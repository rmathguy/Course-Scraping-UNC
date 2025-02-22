# %% Main {{{
def main(COURSE_LIST, EmailVarh

    start_time = time()
    lenn = len(COURSE_LIST)  # To give an idea of how far we are later

    # Excel Stuff {{{

    Excel_info = EXCEL_START_FUNC.ExcelSpreadsheet()
    # Unpack the object
    WS = Excel_info[1]
    WB = Excel_info[0]

    # }}}

    # Driver {{{
    driver = Webpage_and_Driver_Start.main(EmailVar)  # }}}

    #  Iterate on the Courses:# {{{
    '''Loop over the Function'''
    for i, CC in enumerate(COURSE_LIST):

        value_label = ttk.Label(root,
                                text= update_progress_label(
                                            CC, start_time, lenn, i)
                                )
        value_label.grid(column=0, row=1, columnspan=2)

        sleep(1)

        try:
            Page_Search_Excel_Add.main(CC, driver, WS, EmailVar)
            progress(CC, start_time, lenn, i, value_label)
        except Exception:
            try:
                sleep(5)
                Page_Search_Excel_Add.main(CC, driver, WS, EmailVar)
                progress(CC, start_time, lenn, i, value_label)
            except Exception:
                sleep(10)
                Page_Search_Excel_Add.main(CC, driver, WS, EmailVar)
                progress(CC, start_time, lenn, i, value_label)
        if i == 0:
            root.deiconify()
            root.update()


    # Close the Webpage {{{
    driver[0].quit()
    # }}}

    # SAVES THE DATA TO AN EXCEL FILE{{{
    '''ONLY USE BELOW WHEN READY'''
    '''======================
        TODO
    Author: rmathguy
    02-21-25 (M-D-Y)
    Change to a catch exceptions version that will save progress even when the
    program crashes.
    '''

    WB.save(save_name)
    # }}}

    # Runtime Info{{{

    # }}}
# }}}


# %% Imports{{{
'''Only needed if you want to measure how long it takes'''
from time import time  # timing purposes only
from time import sleep
# above makes sure it doesn't get kicked for accessing the site too much

# CUSTOM CODE IMPORTS
import Page_Search_Excel_Add
import EXCEL_START_FUNC
import Webpage_and_Driver_Start

from progress_bar import progress_bar

# For extra windows.
from tkinter import ttk
# }}}
