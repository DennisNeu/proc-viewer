
def main():
    with open("/proc/uptime", "r") as file:
        content = file.read().split()
        # I use content[0] because split turns the string into an array split by whitespace
        minutes = round(float(content[0]) / 60)
        seconds = round(float(content[0]) % 60)
        print(f"The system has been running for {minutes}:{seconds}")
    

if __name__ == "__main__":
    main()