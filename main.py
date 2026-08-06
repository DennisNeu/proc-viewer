def main():
    with open("/proc/uptime", "r") as file:
        content = file.read().split()
        # I use content[0] because split turns the string into an array split by whitespace
        time = float(content[0])
        minutes = round(time / 60)
        seconds = round(time % 60)
        print(f"The system has been running for {minutes} minutes and {seconds} seconds")
    

if __name__ == "__main__":
    main()