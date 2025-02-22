from easyguiu import ynbox  # For the pop-up dialog


def poll_emails():
    boolAnswer = ynbox(msg='Get Instructor Emails?', title=' ',
                               choices=('[<F1>]Yes', '[<F2>]No'),
                               image=None, default_choice='[<F1>]Yes')
    return boolAnswer

