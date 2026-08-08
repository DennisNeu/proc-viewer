"""Handles memory"""
from helper import kb_to_gib

def memory():
    """makes the calculations and prints the relevant memory data"""
    data = get_data()

    total_memory = kb_to_gib(data["MemTotal"])
    available_memory = kb_to_gib(data["MemAvailable"])
    used_memory = total_memory - available_memory
    usage_percentage = used_memory / total_memory * 100

    print(f"Total memory: {total_memory:.2f} GiB")
    print(f"Available memory: {available_memory:.2f} GiB")
    print(f"Used memory: {used_memory:.2f} GiB")
    print(f"Used: {usage_percentage:.2f} %")

def get_data():
    """gets the data from /proc/meminfo and returns a dict
    
       numbers are in kB
    """
    data = {}

    with open("/proc/meminfo", "r") as file:
        for line in file:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().removesuffix(" kB")
            value = int(value)
            data[key] = value

    return data

if __name__ == "__main__":
    memory()