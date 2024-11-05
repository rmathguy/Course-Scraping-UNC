from name_fixer import Name_Fix
from Email_finder import EF

cols_wanted = [0]

def scrape(HTMLFILE,Course_Code,drvr, Cells, EmailVar):
    (No_email_cell, No_email_cell2, No_course_cell, No_name_cell) = Cells
    saved_data = []

    Email_Hash = dict()

    ROWS = HTMLFILE.select('tr')
    for rownum, Row in enumerate(ROWS[1:]):
        # Get the Course Number:{{{
        Course_Num_HTML = Row.findAll('td', {'rowspan': True})

        elements = Row.select('td')
        # Get all cell elements starting from the last{{{
        Cell_list = 13*[[]]
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
        # Get the section number
        try:
            Num_var = int(elements[-11].contents[0])
        except Exception:
            Num_var = 1

        if (Num_var < 300):  # CHECKS to see if the section is not a lecture
            # got the info on what course numbers were lectures from here:
            # https://registrar.unc.edu/academic-services/policies-procedures/university-policy-memorandums/upm-4-standard-course-numbering-system/
            # }}}

            # Name{{{
            NAME = Cell_list[-2]
            # add the email

            try:
                name_tuple = Name_Fix(NAME)
            except Exception:
                name_tuple = ('Error', 'Error')
            try:
                (NameStr, Email) = Email_Hash[name_tuple]
            except Exception:
                (NameStr, Email) = EF(name_tuple, drvr, No_email_cell, No_email_cell, No_course_cell, No_name_cell, EmailVar)
                Email_Hash[name_tuple] = (NameStr, Email)

            # }}
            savethis = Cell_list + [NameStr, Email]
            saved_data.append(savethis)

    # Error Prevention {{{
    if saved_data == []:
        saved_data = [[Course_Code,No_course_cell]]  # }}}

    return saved_data
