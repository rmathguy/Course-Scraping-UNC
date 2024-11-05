# %% Imports{{{
'''Only needed if you want to measure how long it takes'''
from time import time  # timing purposes only
from time import sleep
# above makes sure it doesn't get kicked for accessing the site too much

# CUSTOM CODE IMPORTS
import Page_Search_Excel_Add
import EXCEL_START_FUNC
import Webpage_and_Driver_Start

# For saving file location.
import easygui

# }}}


# %% Main {{{
def main(COURSE_LIST, EmailVar):
    save_name = easygui.filesavebox(default = "save.xlsx", filetypes=["*.xlsx"])

    if save_name is None:
        easygui.exceptionbox("You must choose a save file name", "Note")
        save_name = easygui.filesavebox(default = "save.xlsx", filetypes=["*.xlsx"])
        if save_name is None:
            return

    start_time = time()

    # Excel Stuff {{{

    (Excel_info, Cells) = EXCEL_START_FUNC.ESF()
    WS = Excel_info[1]
    WB = Excel_info[0]

    # }}}

    # Driver {{{
    driver = Webpage_and_Driver_Start.main(EmailVar)  # }}}

    #  Iterate on the Courses:# {{{
    farthest = len(COURSE_LIST)  # To give an idea of how far we are later
    '''Loop over the Function'''

    for i, CC in enumerate(COURSE_LIST):
        sleep(1)
        try:
            Page_Search_Excel_Add.main(CC, driver, WS, Cells, EmailVar)
        except Exception:
            try:
                sleep(5)
                Page_Search_Excel_Add.main(CC, driver, WS, Cells, EmailVar)
            except Exception:
                input("Press Enter to continue when the webpage has loaded.")
                Page_Search_Excel_Add.main(CC, driver, WS, Cells, EmailVar)

        # Display Book-keeping {{{
        time_ellapsed = time()-start_time

        fractiondone = (i+1)/farthest

        timeleft = (1 / fractiondone - 1) * time_ellapsed

        print(CC, "Sucessful", '\t', str(int(100*fractiondone))+"%",
              '\t', str(int(time_ellapsed))+'s',
              '\t', 'Est. Time Left:'+str(int(timeleft))+'s')        # }}}}}}

    # Close the Webpage {{{
    driver[0].quit()  # }}}

    # SAVES THE DATA TO AN EXCEL FILE{{{
    '''ONLY USE BELOW WHEN READY'''

    WB.save(save_name)  # }}}

    # Runtime Info{{{
    print("ALL DONE!")
    print("--- %s seconds ---" % (time() - start_time))

    # }}}
# }}}
