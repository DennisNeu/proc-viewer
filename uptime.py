from math import floor

def uptime():
    with open("/proc/uptime", "r") as file:
        content = file.read().split()
        file.close()

    # I use content[0] because split turns the string into an array split by whitespace
    time = float(content[0])

    # Floor rounds down
    hours = floor(time / 3600)
    minutes = round((time - hours * 3600) / 60)
    seconds = round(time % 60)
    print(f"The system has been running for {hours} hours, {minutes} minutes and {seconds} seconds")
 