import tkinter as tk


def get_Semester():

    frame = tk.Tk()
    frame.title("TextBox Input")
    frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget
    def Input(event):
        global semesterPASS
        semesterPASS = inputtxt.get(1.0, "end-1c")
        inputtxt.quit()


# TextBox Creation
    inputtxt = tk.Text(frame,
                       height=5,
                       width=20)

    inputtxt.pack()
    inputtxt.bind('<Return>', Input)
# Button Creation
    Button = tk.Button(frame,
                       text="Submit")
    Button.pack()
    Button.bind('<Button-1>', Input)
# Label Creation
    lbl = tk.Label(frame, text="Which Semester?")
    lbl.pack()
    frame.mainloop()
    frame.destroy()
    return (semesterPASS)
