from time import time
from datetime import timedelta
import tk


def progress_bar():
    root = tk.Tk()
    root.geometry('500x120')
    root.title('Scraping Progress Bar')

    root.withdraw()

    def update_progress_label(CC, start_time, lenn, i):
        time_ellapsed = time()-start_time
        if i == -1:
            timeleft = 0
        else:
            timeleft = (lenn / (i+1) - 1) * time_ellapsed
        return (str(CC) + " Successful \t " + f"{int(pb['value'])} % " +
                '\t Est. Time Left:'+str(timedelta(seconds=int(timeleft))))

    def progress(CC, start_time, lenn, i, label):
        if pb['value'] < 100:
            pb['value'] = (i+1) * 100 / lenn
            label['text'] = update_progress_label(CC, start_time, lenn, i)
        root.update()

    # progress bar
    pb = ttk.Progressbar(
        root,
        orient='horizontal',
        mode='determinate',
        length=250,
        takefocus=True
    )
    # place the progress bar
    i = -1
    VL = ttk.Label(root, text=update_progress_label("", start_time, lenn, i))
    progress("", start_time, lenn, i, VL)
    pb.grid(column=0, row=0, columnspan=2, padx=150, pady=20)
