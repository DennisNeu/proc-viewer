"""Module that handles processes"""
import os
PATH = "/proc"

class Process:
    """represents a linux process and retrieves relevant info from proc"""

    def __init__(self, pid):
        self.pid = pid
        self.name = self._get_name()

    def _get_name(self):
        return

    def _read_status(self):
        return

def processes():
    """Main function"""
    pids = get_PIDs()

    number_of_processes = len(pids)

    print(f"Total amount of processes: {number_of_processes}")

def get_PIDs():
    """returns a list of all running processes
    
    Processes are represented in /proc by folders with integers as their name

    every interger represents a processes (PID)

    """
    try:
        # Returns only the directories
        directories = os.listdir(PATH)

        pids = []

        # Loop over each dir, if it is an integer, its a PID
        for directory in directories:
            if directory.isdigit():
                pids.append(int(directory))

        return pids

        

    except OSError as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    processes()
