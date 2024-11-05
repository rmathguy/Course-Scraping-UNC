# %% Page Search Excel Add{{{
from search_in_page import sip
from scraper2 import scrape


def main(CC, Driver_info, WS, Cells, EmailVar):
    # Make less inputs{{{
    if EmailVar is True:
        (Drive,  WINDOW, secondtab) = Driver_info
    # (No_email_cell, No_email_cell2, No_course_cell, No_name_cell) = Cells  # }}}
    else:
        (Drive,  WINDOW) = Driver_info

    # GO BACK TO THE FIRST TAB
    Drive.switch_to.window(WINDOW)

    # Get the HTML of the page:
    soup = sip(CC, Drive)

    # Switch To the Directory search tab for the name lookup in the function
    if EmailVar is True:
        Drive.switch_to.window(secondtab)

    datatoadd = scrape(soup, CC, Drive, Cells, EmailVar)

    # ADDS The DATA TO A Workbook
    for row in datatoadd:
        WS.append(row)
# }}}
