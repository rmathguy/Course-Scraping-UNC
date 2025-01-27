def scraper(HTMLFILE,Course_Code,DRIVER,Cells,EmailVar):
    (No_email_cell,No_email_cell2,No_course_cell,No_name_cell) = Cells
    saved_data = []
    ROWS = HTMLFILE.select('tr')
    counter = -1 # initializes to -1 because it adds 1 if the test case is good
    for rownum,Row in enumerate(ROWS[1::]):
        ''' NEED to move this all from Regex to BS4''' 
        for excel_col_num,page_col_num in enumerate(Cols_Wanted):
            Row_html_txt = str(Row)
            
            
            data = Dynamic_REGEX[excel_col_num].search(Row_html_txt) #load the regular expression for that column and search for it
             
            try:
                temporary = data.group()
            except:
                temporary = "0"
            
            '''
            CHANGE HERE TO BE THE BS4 Component finder things
            
            CHANGE HERE TO BE THE BS4 Component finder things
            
            CHANGE HERE TO BE THE BS4 Component finder things
            '''
            temporary = re.sub(FirstREGEX,"",temporary) #load the 1st cleaning regex and remove the parts I don't want
            
            temporary = re.sub(SecondREGEX,"",temporary)#load the 2nd cleaning regex and remove the parts I don't want
            
            temporary = re.sub(LastREGEX,"",temporary)#load the last cleaning regex and remove the parts I don't want
            
            if (excel_col_num == 0):
                try:
                    Num_var = int(temporary)
                except:
                    break
                
                if (Num_var > 300): #CHECKS to see if the section is not a lecture
                    break
                    #got the info on what course numbers were lectures from here: 
                    #https://registrar.unc.edu/academic-services/policies-procedures/university-policy-memorandums/upm-4-standard-course-numbering-system/
                else:
                    counter += 1
                    saved_data.append([Course_Code])
            else:
                saved_data[counter].append(temporary)
        
            
            if (excel_col_num == 5):
                NAME = saved_data[-1][-1]
                # add the email
                
                try:
                    name_tuple = Name_FIXER(NAME)
                except:
                    print(NAME)
                    name_tuple = ('ERROR','ERROR')
                    #name_tuple = ("Name Not","Parsable")
                
                for ind,part in enumerate(Email_finder(name_tuple,DRIVER,No_email_cell,No_email_cell2,No_course_cell,No_name_cell,EmailVar)): 
                    if ind == 0:
                        saved_data[counter][-1] = part
                    else:
                        saved_data[counter].append(part)


            
    if saved_data == []:
        saved_data =[[Course_Code,No_course_cell]]
        
    return saved_data
