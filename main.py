"""Main function for a learning project getting data from /proc
   
   system information tool
"""

from uptime import uptime
from memory import memory

def main():
        uptime()
        memory()

if __name__ == "__main__":
    main()