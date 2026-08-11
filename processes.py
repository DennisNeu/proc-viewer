"""Module that handles processes"""
import os
from helper import kb_to_mib
PATH = "/proc"

class Process:
    """represents a linux process and retrieves relevant info from proc"""

    def __init__(self, pid):
        self.pid = pid
        self._status = self._read_status()
        self.name = self._status["Name"]
        self.state = self._status["State"]
        self.ppid = int(self._status["PPid"])
        self.threads = int(self._status["Threads"])
        print(self._status)
        self.memory = self._status.get("VmRSS")

    def __str__(self):
        return f"{self.pid}: {self.name}"

    def __repr__(self):
        return f"{self.pid}: {self.name}"

    def _read_status(self):
        """gets the data from /proc/<pid>/status and returns a dict
        
        numbers are in kB
        """
        data = {}

        with open(f"/proc/{self.pid}/status", "r") as file:
            for line in file:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().removesuffix(" kB")

                if key == "VmRSS":
                    value = round(kb_to_mib(value))

                data[key] = value

        return data

    

def processes():
    """Main function"""
    pids = get_pids()

    number_of_processes = len(pids)

    print(f"Total amount of processes: {number_of_processes}")

def get_pids():
    """returns a list of all running processes
    
    Processes are represented in /proc by folders with integers as their name

    every interger represents a processes (PID)

    """
    try:
        # Returns contents of /proc
        content = os.listdir(PATH)

        pids = []

        # Loop over each dir, if it is an integer, its a PID
        for item in content:
            if item.isdigit():
                pids.append(int(item))

        return pids

        

    except OSError as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    processes()
