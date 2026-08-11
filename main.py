"""Main function for a learning project getting data from /proc
   
   system information tool
"""

from uptime import uptime
from memory import memory
from processes import get_pids, Process

def main():
        uptime()
        memory()

        pids = get_pids()
        number_of_processes = len(pids)
        print(f"Total amount of processes: {number_of_processes}")

        processes = []

        for PID in pids:
              processes.append(Process(PID))

        for process in processes:
              print(f"{process.pid}: {process.name} state: {process.state} PPid: {process.ppid} Threads: {process.threads} Memory: {process.memory}")

        

if __name__ == "__main__":
    main()