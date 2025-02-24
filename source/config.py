import easygui  # For Graphical Pop-ups
import configparser  # For Config file handling.


config = configparser.ConfigParser()


'''
======================
    TODO
Author: rmathguy
01-27-25 (M-D-Y)
Finish the read configuration function
'''


"""
config.py
====================================
The config handler module for this program.
"""


def read_config():
    """
    Given a config file read out the contents into variables for use.
    """

    config = configparser.ConfigParser()

    return config


def poll_config():
    hasConfig = easygui.ynbox(msg='Get Configuration File?', title=' ',
                              choices=('[<F1>]Yes', '[<F2>]No'),
                              image=None, default_choice='[<F1>]Yes')

    if hasConfig:
        return read_config(get_config())

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


def save_config():
    config_file = easygui.filesavebox(
                    msg="Choose where to save the configuration file.",
                    filetypes=["*.cfg"],
                    default="*.cfg"
                    )

    with open(config_file, 'w') as configfile:
        config.write(configfile)
