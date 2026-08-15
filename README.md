# proc-viewer
Simple python application to read system information from the dynamic /proc linux file system

## What is proc?
`/proc` is a virtual filesystem within Linux environments. The kernel exposes live system information through this filesystem. The user and processes can access the `/proc` filesystem to get details on memory, CPU usage, running processes etc. These files are generated "on the fly" by the kernel.

Exploring `/proc` is easy:
```bash
cd /proc
ls
```

Use `cat` to view exposed files. 

For more info, view:

https://wiki.archlinux.org/title/Procfs

## Currently supports:
- displaying memory information
- system uptime
- details about running processes

## How to install:

1. Clone this repo by running this command in your shell (git must be installed):
```bash
git clone https://github.com/DennisNeu/proc-viewer.git
```

2. Change shell's working directory into downloaded directory:
```bash
cd proc-viewer
```

3. Setup virtual environment. This keeps the project's dependencies separate from system wide python packages. Installing packages directly into the global Python environment isn't the convention anyways:
```bash
python -m venv venv
```

**Hint:**
make sure the necessary dependency is installed:
```bash
sudo apt install python3-venv
```

4. Activate the virtual environment. The exact command depends on the **shell**. If using bash, run:
```bash
source venv/bin/activate
```

If using fish, run:
```bash
source venv/bin/activate.fish
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

**Hint:**
This requires **pip** to be installed. Pip is a package manager for Python packages. To install it on systems using apt (like debian or ubuntu):
```bash
sudo apt update
sudo apt install python3-pip
```

On arch based systems with pacman:
```bash
sudo pacman -S python-pip
```

6. run the application:
```bash
python main.py
```

**Hint:**
The virtual environment can be left with:
```bash
deactivate
```
