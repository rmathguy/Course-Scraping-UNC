import csv
import easygui


csv_file = easygui.fileopenbox(msg = "Choose Course CSV", filetypes=["*.csv"])

def read_csv():
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        Course_List = list(reader)

    output = list()

    for i, line in enumerate(Course_List):
        try:
            output.append(line[0] + " " + line[1])
        except Exception:
            output.append(line[0])

    return output
