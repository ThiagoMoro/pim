from datetime import datetime

LOG_FILE = 'log.txt'

def log(message: str):
    """Append a timestamp message to LOG_FILE."""
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    line = f"{timestamp} - {message}\n"
    with open(LOG_FILE, 'a') as f:
        f.write(line)
