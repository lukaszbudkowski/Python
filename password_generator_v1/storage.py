import datetime

history = []

def add_to_history(password):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append((timestamp, password))

def export_history(filename="password_history.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for timestamp, password in history:
            f.write(f"{timestamp} - {password}\n")
