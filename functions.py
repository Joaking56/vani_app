def open_wanted_file():
    with open("wanted.txt", "r", encoding="utf-8") as f:
        items = f.readlines()
        return items

def write_wanted_file(wanted_item):
    with open("wanted.txt", "w", encoding="utf-8") as f:
        f.writelines(wanted_item)

def open_completed_file():
    try:
        with open("completed.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def write_completed_file(completed_items):
    with open("completed.txt", "w", encoding="utf-8") as f:
        f.writelines(completed_items)