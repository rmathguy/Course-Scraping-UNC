import easygui


def get_Semester():
    semesterPass = easygui.enterbox("Which Semester Formmated as 'YYYY Season'",
                                    "Semester Prompt", "")
    return(semesterPass)
 
