"""Main function for a learning project getting data from /proc
   
   system information tool

   This class is designed to be the launcher
"""

from uptime import uptime
from memory import memory
from processes import _get_pids, Process
from ui import ProcViewerApp

def main():
      app = ProcViewerApp()
      app.run()
        

if __name__ == "__main__":
    main()