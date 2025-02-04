import main
from csv_reader import read_csv
from get_emails import poll_emails
from config import poll_config

poll_config()


main.main(read_csv(), poll_emails())
