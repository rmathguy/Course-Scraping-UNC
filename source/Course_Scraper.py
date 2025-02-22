from main import main
from csv_reader import read_csv
from config import poll_config
from easygui import ynbox  # For the pop-up dialog

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
    :rtype: Bool
    '''
    boolAnswer = ynbox(msg='Get Instructor Emails?', title=' ',
                               choices=('[<F1>]Yes', '[<F2>]No'),
                               image=None, default_choice='[<F1>]Yes')
    return boolAnswer

# poll_config()


# main.main(read_csv(), poll_emails())
