import main
from csv_reader import read_csv
from config import poll_config
from easygui import ynbox  # For the pop-up dialog
import EXCEL_START_FUNC

"""
Course_Scraper.py
-------------
This is the main Kahuna
Holds the setup and eventually clean up for the program.
"""


def poll_emails():
    '''
    Use the Yes-No-Box to prompt the end user if they want to also find the
    instructor emails on the directory.
    :params: No Inputs Needed
    :returns: A Boolean Saying whether or not to get the emails.
    :rtype: Boolean
    '''
    boolAnswer = ynbox(msg='Get Instructor Emails?', title=' ',
                           choices=('[<F1>]Yes', '[<F2>]No'),
                           image=None, default_choice='[<F1>]Yes'
                       )
    return boolAnswer


'''
======================
    TODO
Author: rmathguy
02-22-25 (M-D-Y)
Actually make a config reader/writer and incorporate it into the packaging
I've done thus far.
'''

# poll_config()


def final_runme():
    """
    The runtime main function.

    :returns: NoneType it writes a file onto the file system of the output.
    """
    # Excel Stuff {{{
    Excel = EXCEL_START_FUNC.ExcelSpreadsheet()

    WB = Excel[0]  # Unpack it a bit for later processing (when saving)
    # }}}


    poll_config()
    try:
        main.main(read_csv(), poll_emails(), Excel)
    except Exception:
        WB.save(save_name)  # SAVES THE DATA TO AN EXCEL FILE{{{
