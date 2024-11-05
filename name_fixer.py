import re
#These Regexs sort out between the first and last name in the way it's formatted on the page we parse
First_Name_REGEX = re.compile(r',\w*')
Last_Name_REGEX = re.compile(r'.*,')

#Finds the Commas and white-spaces to be eventually removed at the right time.
REMOVE_comma_REGEX = re.compile(r',')
Remove_whitespace_REGEX = re.compile(r'(\s(\S*))$')


# %% White Space{{{
    
def white_space_remover(NAME):
    '''
    Input: NAME
    
    Output: Name witout Whitespaces
    '''
    try:
        thing  = Remove_whitespace_REGEX.search(NAME)
        thing = thing.group()
        # making sure it doesn't match the whole string
        if thing == NAME:
            NAME_USE = NAME
        else:
            NAME_USE = re.sub(Remove_whitespace_REGEX,"",NAME)
    except:
        NAME_USE = NAME
        
    return NAME_USE

# }}}


# %% Name_Fixer{{{
def Name_Fix(NAME):
    if NAME == "\n"+'None' or NAME == 'None':
        first_name = 'No Instructor'
        last_name  = 'Listed'
    else:
        #find the first name
        temporary = First_Name_REGEX.search(NAME)
        # Isolate it
        first_name = temporary.group()

        #Find the last name
        temporary = Last_Name_REGEX.search(NAME)
        # Isolate it
        last_name = temporary.group()

        #Removes the white space and middle names
        first_name = white_space_remover(first_name)


        # Removes Commas
        first_name = re.sub(REMOVE_comma_REGEX,"",first_name)
        last_name  = re.sub(REMOVE_comma_REGEX,"",last_name)
        
    return (first_name,last_name)   



# }}}
