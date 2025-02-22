def SearchAndSoupifyPage(COURSE, DRIVER):
    """
    Search in the page using selenium to interact with the page to do the
    following:

    * Find the search bar
    * Type in the Course Code
    * Get the output HTML
    * Return it as a  parsable BeautifulSoup4 soup type.

    :params str COURSE: The Course Code that we are going to search in the
        webpage

    :params selenium.driver DRIVER: The browser driver that enables us to
        interact with the webpage (actual type not correct)

    :return: A BS4 Soup of the webpage after the search was completed

    :rtype: BS4 Soup
    """

    '''FIND THE SEARCH BAR'''
    elem = DRIVER.find_elements(By.CLASS_NAME, "form-control")[0]
    Attr_check_var1 = str(elem.get_attribute("type"))

    # Check we are in the right field VVV
    assert (Attr_check_var1 == "text")  # and Attr_check_var1 == "advanced")
    
    # if so: Clear the search field, enter in the course code and press enter
    elem.clear()
    elem.send_keys(COURSE)  # Enter the Course Cod3
    elem.send_keys(Keys.RETURN)  # Press Enter

    sleep(5)  # Give the page a bit to load and search for the relevant info.

    soup = BeautifulSoup(DRIVER.page_source, features="html.parser")
    return soup

# Imports{{{
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup  # for parsing the html
# }}}
