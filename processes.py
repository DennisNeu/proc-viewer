"""Module that handles processes"""
import os
PATH = "/proc"

def processes():
    """Main function"""
    pid_list = get_processes()

def get_processes():
    """returns a list of all running processes"""
    try:
        # Returns only the directories
        dirs = [d for d in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, d))]

        pid = []

        # Loop over each dir, if it is an integer, its a PID
        for dir in dirs:
            if dir.isdigit():
                pid.append(int(dir))

        return pid

        

    except OSError as e:
        print("Error:", e)

if __name__ == "__main__":
    processes()