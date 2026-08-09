# proc-viewer
Simple python application to read system information from the dynamic /proc linux file system

## What is proc?
`/proc` is a virtual filesystem within Linux enviroments. The kernel exposes live system information through this filesystem. The user and processes can access the `/proc` filesystem to get details on memory, cpu, processes etc. The files are generated "on the fly" by the kernel

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

## How to install:

1. Clone this repo by running this command in your shell (git must be installed):
```bash
git clone git@github.com:DennisNeu/proc-viewer.git
```

2. change shell into downloaded directory:
```bash
cd proc-viewer
```

3. run main function:
```bash
python main.py
```

