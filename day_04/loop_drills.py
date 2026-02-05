#Task 4.1: The Roll Call (Basic Iteration)

ip_list = ["192.168.1.1","10.0.0.1","172.16.0.1"]
for ip in ip_list:
    print(f"Scanning IP: {ip}")

#Task 4.2 : The filter (Loop +If)

port = [80,443,22,21,8080]
for i in port:
    if i == 22:
        print(f"SSH Detected on port {i}")
    else:
        print(f"Port {i} is standard")

#Task 4.3: The Accumulator (Counting)

log_statuses = ["Success","Failed","Success","Failed","Failed","Success"]
failed_count = 0
for i in log_statuses:
    if i == "Failed":
        failed_count = failed_count+1

print(f"Total Failed Logons: {failed_count}")

#Task : The "Muscle Memory" Repetition
files = ["cmd.exe", "report.docx", "powershell.exe", "notes.txt"]
for i in files:
    if ".exe" in i:
        print(f"Suspicious Executable Found: {i}")


#Task : The "Muscle Memory" Repetition - look for ".docx". Write it again, but count how many .exe files
files = ["cmd.exe", "report.docx", "powershell.exe", "notes.txt"]
exe_count = 0
for i in files:
    if ".docx" in i:
        print(f"The file is document and its name is {i}")
    elif ".exe" in i:
        exe_count = exe_count+1
print(f"Total number of exe is {exe_count}")
