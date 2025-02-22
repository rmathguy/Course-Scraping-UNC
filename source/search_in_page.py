# Imports{{{
import bs4  # for parsing the html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
# }}}


def sip(COURSE, DRIVER):
    '''FIND THE SEARCH BAR'''
    elem = DRIVER.find_elements(By.CLASS_NAME, "form-control")[0]
    Attr_check_var1 = str(elem.get_attribute("type"))
    # Attr_check_var2 = str(elem.get_attribute("id"))
    # Check we are in the right field
    assert (Attr_check_var1 == "text")  # and Attr_check_var1 == "advanced")
    # if so: Clear the search field, enter in the course code and press enter
    elem.clear()
    elem.send_keys(COURSE)
    elem.send_keys(Keys.RETURN)

    sleep(5)

    soup = bs4.BeautifulSoup(DRIVER.page_source, features="html.parser")
    return soup
