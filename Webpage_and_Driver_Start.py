# %% Webpage and Driver Start{{{

# IMPORTS
# Imports{{{
'''Import Selenium and key inputs so that we can press "enter" '''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# }}}

def main(EmailVar):
    driver = webdriver.Firefox()
    driver.get("https://reports.unc.edu/class-search/advanced_search/")
    # Website is the one above ^
    # Lets open another tab for direct:ory seach in the second tab
    Class_Search_Window = driver.window_handles[0]
    # Save the window for later changing

    '''THIS SECTION SELECTS THE CORRECT TERMS'''
    # Find the semester list
    elem = driver.find_elements(By.CLASS_NAME, "form-control")[1]
    Attr_check_var1 = str(elem.get_attribute("type"))
    # Attr_check_var2 = str(elem.get_attribute("id"))
    # Check we are in the right field
    assert (Attr_check_var1 == "text" )  # and Attr_check_var1 == "term")
    # if so: Clear the search field, enter in the course code and press enter
    elem.clear()
    elem.send_keys(r"2024 Fall")
    elem.send_keys(Keys.ESCAPE)
    """END SELECTING TERMS"""  
    # If we want to find the email, then open a new tab to search for the email later.
    if EmailVar is True:
        # OPEN A  NEW TAB FOR THE DIRECTORY
        driver.execute_script("window.open('about:blank','secondtab');")
        secondtab = driver.window_handles[1] 
        return (driver, Class_Search_Window, secondtab)

    else:
        return (driver, Class_Search_Window)
# }}}
