# %% Imports{{{
'''Only needed if you want to measure how long it takes'''
from time import time  # timing purposes only
from time import sleep
# above makes sure it doesn't get kicked for accessing the site too much

# CUSTOM CODE IMPORTS
import Page_Search_Excel_Add
import Webpage_and_Driver_Start

from progress_bar import progress_bar

# For extra windows.
from tkinter import ttk
# }}}


def main(COURSE_LIST, EmailVar, Excel):
    """
    The big main function.

    :params list COURSE_LIST: A list of the courses to iterate through, should
        be a list of stings

    :params Bool EmailVar: Find the Emails, Yes or No?

    :params Tuple Excel: The tuple of the Excel workbook then Excel worksheet.

    :returns: NoneType it edits the Excel spreadsheet to save in the outer
        function of final_runme()
    """
    start_time = time()
    lenn = len(COURSE_LIST)  # To give an idea of how far we are later
    WS = Excel[1]

# Driver {{{
    driver = Webpage_and_Driver_Start.main(EmailVar)  # }}}

    #  Iterate on the Courses:# {{{
    '''Loop over the Function'''
    for i, CourseCode in enumerate(COURSE_LIST):

        # value_label = ttk.Label(root,
        #                         text= update_progress_label(
        #                                     CourseCode, start_time, lenn, i)
        #                         )
        # value_label.grid(column=0, row=1, columnspan=2)

        sleep(1)

        try:

            Page_Search_Excel_Add.main(CourseCode, driver, WS, EmailVar)
            # progress(CourseCode, start_time, lenn, i, value_label)

        except Exception:
            try:
                sleep(5)  # Time outs can occur if we probe too much, give it a
                # bit to try again
                Page_Search_Excel_Add.main(CourseCode, driver, WS, EmailVar)
                # progress(CourseCode, start_time, lenn, i, value_label)

            except Exception:
                sleep(10)  # Wait even longer and hope it eventually works lol.

                '''======================
                    TODO
                Author: rmathguy
                02-23-25 (M-D-Y)
                Fix Progress Bar Stuff Below
                '''

                Page_Search_Excel_Add.main(CourseCode, driver, WS, EmailVar)
                # progress(CourseCode, start_time, lenn, i, value_label)

        # if i == 0:
        #    root.deiconify()
        #    root.update()

    # Close the Webpage {{{
    driver[0].quit()
    # }}}
