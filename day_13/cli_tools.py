#Task 13.1: The Argument Echo
import sys
sys_argv = sys.argv
length_of_sys_argv = len(sys.argv)
print(f"This is sys.argv = {sys_argv}")
print(f"Total Number of length is {len(sys_argv)}")

#Task 13.2: The Guard Rail (Input Validation)
'''
if length_of_sys_argv < 2:
    print("Usage: python cli_tools.py <target_ip>")
    sys.exit()

target = sys_argv[1]
print(f"Commencing scan on: {target}")
'''

#Task 13.3: The File Loader (Dynamic File Opening)

if length_of_sys_argv < 2:
    print("Usage: python cli_tools.py <target_ip> <file_name>")
    sys.exit()
file_name = sys_argv[1]
try:
    with open(file_name,"r",encoding="UTF-8",errors="ignore") as f:
        for line in f:
            print((line).strip())
except FileNotFoundError:
    print(f"The {file_name} is not found")