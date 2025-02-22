from easygui import enterbox


def get_Semester():
    """
    Using easygui ask the end user what semester they want using a prompt box.

    :params: Takes No Inputs
    :returns: String containing the semester information as YYYY FA/SP/SM.
    :rtype: str
    """
    semesterPass = enterbox(
            "Which Semester Formmated as 'YYYY Season'", "Semester Prompt", ""
            )
    return semesterPass
