# %% Excel Start Function
def ExcelSpreadsheet():
    """
    Make the Excel Spreadsheet using openpyxl

    :params: This function takes no inputs.
    :returns: A list of the excel workbook and worksheet.
    :rtype: list
    """

    from openpyxl import Workbook  # Creates the excel sheets and workbooks that I will use
    # Start a WRITE ONLY workbook to keep ram usage low
    wb = Workbook(write_only=True)

    # need to create a sheet to start as the workbook is write_only
    ws = wb.create_sheet()

    return [wb, ws]

# }}}

