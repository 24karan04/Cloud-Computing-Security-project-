import datetime

LOG_FILE = "data/logs.txt"

def log_event(event):
    time = datetime.datetime.now()
    with open(LOG_FILE, "a") as f:
        f.write(f"{time} : {event}\n")