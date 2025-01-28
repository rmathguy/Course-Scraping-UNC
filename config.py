import easygui

'''======================
    TODO
Author: rmathguy
01-27-25 (M-D-Y)
Finish the read configuration function
'''

def read_config():
    temp 


def poll_config():
    hasConfig = easygui.ynbox(msg='Get Configuration File?', title=' ',
                               choices=('[<F1>]Yes', '[<F2>]No'),
                               image=None, default_choice='[<F1>]Yes')

    if hasConfig:
        return read_config( get_config() )

    makeConfig = easygui.ynbox(msg='Generate Configuration File??', title=' ',
                               choices=('[<F1>]Yes', '[<F2>]No'),
                               image=None, default_choice='[<F1>]Yes')
    if makeConfig: 
        save_config()



def get_config():
    config_file = easygui.fileopenbox(msg="Choose Config File",
                                   filetypes=["*.cfg"],
                                   default="*.cfg")
    return config_file


def save_confiig():


