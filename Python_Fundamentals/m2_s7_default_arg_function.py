def filter_logs(lines, level='ERROR'):

    """Return lines matching level"""
    #list comprehension to filter the lines based on the level
    #first argument is new list to be created, second is the loop to iterate through the lines, and third is the condition to check if the level is in the line
    return [ln for ln in lines

    if level in ln]


# Usage

logs = ["[INFO] Start","[ERROR] DB Fail"]

print(filter_logs(logs))