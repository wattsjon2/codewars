# take a given number of seconds and turn it into hh:mm:ss time

def make_readable(seconds):
    hours = 0
    minutes = 0
    if seconds >= 3600:
        hours = seconds // 3600
        seconds = seconds % 3600
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"