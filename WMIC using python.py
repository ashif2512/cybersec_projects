import platform
import os

def bios_version():
    uname_result = platform.uname()
    return f"BIOS version: {uname_result.version}"

save_path = 'D:/'
name_of_file = input("What is the name of the file: ")
completeName = os.path.join(save_path, name_of_file + ".txt")

with open(completeName, "w") as f:
    f.write(bios_version())

print(f"BIOS version saved to {completeName}")
