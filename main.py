"""Main function for a learning project getting data from /proc
   
   system information tool
"""

from uptime import uptime
from memory import memory
from processes import processes

def main():
        uptime()
        memory()
        processes()

if __name__ == "__main__":
    main()