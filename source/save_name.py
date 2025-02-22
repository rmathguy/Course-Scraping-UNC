from sys import exit # Needed to break if no name would be given
import easygui # Needed for the nice boxes on all OSes

def get_save_name();
    save_name = easygui.filesavebox(default="save.xlsx", filetypes=["*.xlsx"])

    if save_name is None:
        easygui.exceptionbox("You must choose a save file name", "Note")
        save_name = easygui.filesavebox(default="save.xlsx", filetypes=["*.xlsx"])
        if save_name is None:
            exit()
    return save_name


