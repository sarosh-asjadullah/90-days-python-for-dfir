
import os
import time



#TASK 10.1: The Recon (Where am I?)
print(f"TASK 10.1: The Recon (Where am I?)")
cwd = os.getcwd()

print(f"Current Analysis Directory is: {cwd}")
files = os.listdir(cwd)
print(f"Files found: {files}")

#Task 10.2: The Evidence Validator
print(f"\nTask 10.2: The Evidence Validator")
target_file = __file__ # __file__ is a built-in variable that contains the path of the current Python script. Here, target_file is being set to the filename (or full path) of the running file.
file_name = os.path.basename(target_file) # os.path.basename(full_path) It automatically extracts the filename from a path on any operating system.
if os.path.exists(target_file):
    size = os.path.getsize(target_file)
    print(f"Target found {file_name} - Size: {size} bytes")
else:
    print("Target Missing")



#Task 10.3: The Timestamp Generator
print(f"\nTask 10.3: The Timestamp Generator")

print(f"Scan Started at : {time.ctime()}")
time.sleep(2)
print(f"Scan Finished at : {time.ctime()}")


#TASK The "Muscle Memory" Gauntlet (The Directory Scanner)
print(f"\nTask 10.3:The Muscle Memory Gauntlet (The Directory Scanner)")

cwd = os.getcwd()
found = False
for name in os.listdir(cwd):
    if name.endswith(".py"):
        found = True
        full_path = os.path.join(cwd, name)
        size = os.path.getsize(full_path)
        print(f"[SCRIPT] {name} | {size} bytes")
if not found:
    print("No python file found")















