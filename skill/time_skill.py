import datetime

def run(text=None):
    now = datetime.datetime.now().strftime("%H:%M")
    return f"The time is {now}"