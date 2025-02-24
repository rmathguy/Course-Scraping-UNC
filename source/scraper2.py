from name_fixer import Name_Fix
import Email_Finder
from openpyxl.cell import WriteOnlyCell  # To edit cell attributes
from openpyxl.styles import PatternFill  # Cell Color Fills


def scrape(HTML, Course_Code, driver, EmailVar):
    """
    Takes the HTML as soup and the Course_Code,
    the driver and var determining if we
    get the email.

    Does some analysis on whether or not to keep a course that we are scanning
    for, generally the ones we know won't be relevant like lab sections etc.

    Uses the name fixer function from the name_fixer module to correct the
    names for searching.

    :params bs4.soup HTML: The BeautifulSoup4 soup for the webpage of courses
        etc.

    :params str Course_Code: A string of the Course Code in plain text.

    :params selenium.driver DRIVER: The selenium browser driver used.

    :params Bool EmailVar: Get the Emails? True or False?

    :returns: The data to write to the excel sheet/workbook.
    :rtype: list of lists
    """
    "COURSE NOT OFFERED CELL"

    No_course_cell = WriteOnlyCell(ws, value="No Sections Offered")
    yellowFill = PatternFill(start_color='FDF96F', end_color='FDF96F',
                             fill_type='solid')

    No_course_cell.fill = yellowFill
    # End Cell Stuff.

    saved_data = []  #Create and empty list of the data to save later.

    Email_Hash = dict()  # Create a dictionary to 'cache' an email
    # given a name

    ROWS = HTML.select('tr')

    for rownum, Row in enumerate(ROWS[1:]):
        # Get the Course Number:{{{
        '''
        Is the below line neede?
        '''
        # Course_Num_HTML = Row.findAll('td', {'rowspan': True})

        elements = Row.select('td')

        # Get all cell elements starting from the last{{{
        Cell_list = 13 * [ [] ]
        Cell_list[0] = Course_Code

        # Course Number Check{{{
        # Get the section number
        try:
            CourseNum = int(elements[-13].contents[0].get_text())
            SavedVar = CourseNum
        except Exception:
            try:
                CourseNum = SavedVar
            except Exception:
                CourseNum = 000
                SavedVar = CourseNum

        if CourseNum > 599:

            break
        if CourseNum == 395 or CourseNum == 495:
            continue

        Cell_list[1] = CourseNum
        # }}}

        # Grab the last 11 Columns
        # print(elements)
        for ind in range(11):
            Cell_list[-ind-1] = elements[-ind-1].contents[0]
        # }}}

        # Course Section Check{{{

        ''' Get the section number '''
        try:
            Num_var = int(elements[-11].contents[0])
        except Exception:
            Num_var = 1  # Need to set it to something for later stuff, don't
            # want to lose something if it might be needed

        if (Num_var < 300):  
            ''' CHECKS to see if the section is not a lecture 
            # got the info on what course numbers were lectures from here:
            # https://registrar.unc.edu/academic-services/policies-procedures/university-policy-memorandums/upm-4-standard-course-numbering-system/
            # }}} Name{{{
            '''
            NAME = Cell_list[-2]
            # add the email
            
            '''
            ======================
                TODO
            Author: rmathguy
            02-22-25 (M-D-Y)
            There is some better way to structure this part with the emails
            I'm sure.

            Right now it has it that it still uses the Email_Finder funciton
            even when we should know not to because EmailVar == False.

            Seems right now the only reason why is because we want the
            No_email_cell2

            '''
            try:
                # Try and standardize the name.
                name_tuple = Name_Fix(NAME)
            except Exception:
                name_tuple = ('Error', 'Error')
            try:
                # See if we get a 'hash hit'
                (NameStr, Email) = Email_Hash[name_tuple]
            except Exception:
                # If not find the email hash it and add to the dictionary.
                (NameStr, Email) = Email_Finder.EmailFinder(name_tuple, driver, EmailVar)
                Email_Hash[name_tuple] = (NameStr, Email)

            # }}
            savethis = Cell_list + [NameStr, Email]
            saved_data.append(savethis)

    # Error Prevention {{{
    if saved_data == []:
        
        saved_data = [ [Course_Code, No_course_cell] ]  
    # }}}

    return saved_data


