import datetime
import os

LOG_FILE = "data/logs.txt"

def log_event(event):
    os.makedirs("data", exist_ok=True)

    time = datetime.datetime.now()
    with open(LOG_FILE, "a") as f:
        f.write(f"{time} : {event}\n")