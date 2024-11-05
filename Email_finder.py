# %% Email Finder{{{
from time import sleep
import bs4


def EF(NAME_TUPLE, DRIVER, No_email_cell, No_email_cell2,
       No_course_cell, No_name_cell, EmailVar):

    firstName = NAME_TUPLE[0]
    lastName = NAME_TUPLE[1]
    if firstName == 'No Instructor':
        return [No_name_cell, No_email_cell2]
    else:
        if EmailVar is True:
            DRIVER.get('https://dir.unc.edu/search/'+firstName+'%20'+lastName)
            sleep(1)
            if " If the error indicates a time limit" in DRIVER.page_source or "This page isn’t working" in DRIVER.page_source:
                sleep(5)
                return EF(NAME_TUPLE, DRIVER, No_email_cell,
                          No_email_cell2, No_course_cell,
                          No_name_cell, EmailVar)
            else:
                # Check to make sure something was found
                if "no results" not in DRIVER.page_source:
                    # save the page
                    soup_file = DRIVER.page_source
                    soup = bs4.BeautifulSoup(soup_file, 'html.parser')

                    email_link = soup.select('a[href^=mailto]')

                    try:
                        href = email_link[0]['href']

                        try:
                            str1, email = href.split(':')
                        except ValueError:
                            return [firstName + " " + lastName, No_email_cell]

                        # if it does work return the email
                        return [firstName + " " + lastName, email]
                    except IndexError:
                        return [firstName + " " + lastName, No_email_cell]
                else:
                    return [firstName + " " + lastName, No_email_cell]
        else:
            return [firstName + " " + lastName, No_email_cell2]


# }}}
