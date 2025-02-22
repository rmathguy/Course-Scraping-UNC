# %% Page Search Excel Add{{{
from search_in_page import SearchAndSoupifyPage
from scraper2 import scrape


def main(CC, Driver_info, WS, Cells, EmailVar):
    '''
    Loads the webpage and  search within in it for the *Course Information* 

    
    :params   : No Inputs Needed
    :returns: A Boolean Saying whether or not to get the emails.
    :rtype: Bool
    '''

    # Make less inputs{{{
    if EmailVar is True:
        (Drive,  WINDOW, secondtab) = Driver_info

    # }}}
    else:
        (Drive,  WINDOW) = Driver_info

    # GO BACK TO THE FIRST TAB
    Drive.switch_to.window(WINDOW)

    # Get the HTML of the page:
    soup = SearchAndSoupifyPage(CC, Drive)

    # Switch To the Directory search tab for the name lookup in the function
    if EmailVar is True:
        Drive.switch_to.window(secondtab)

    # Save the data later.
    datatoadd = scrape(soup, CC, Drive, EmailVar)

    # ADDS The DATA TO A Workbook
    for row in datatoadd:
        WS.append(row)
# }}}
