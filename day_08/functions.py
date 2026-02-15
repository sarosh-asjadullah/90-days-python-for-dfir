# Drill 8.1: The Sanitize Function
def clean_artifact(artifact):
    cleaned = artifact.strip().lower()
    return cleaned

print(clean_artifact(" Malware.EXE "))

#Drill 8.2: The IOC Checker (Boolean Returns)

def is_critical_ip(ip_adress):
    if "192.168" in ip_adress:
        return(False)
    else:
        return(True)

ip_list = ["192.168.1.14","192.168.42.119","8.44.12.159","192.168.254.210","172.217.14.206","192.168.15.22","185.199.108.153","192.168.77.141","93.184.216.34","164.233.191.100"]

for i in ip_list:
    print(f"Checking {i}: Critical? {is_critical_ip(i)}")

#Drill 8.3: The Log Parser (Function with Multiple Returns)

def parse_log_line(line):
    split_line = []
    split_line = line.split(" ")
    timestamp = split_line[3].strip("[]")
    ip = split_line[0]
    return(timestamp,ip)

sample = '10.0.0.5 - - [10/Oct/2023]'
time, ip = parse_log_line(sample)
print(f"Time: {time} | IP: {ip}")


#TASK The “Muscle Memory” Gauntlet

def extract_ip_time(line): # It takes a line and returns the IP
    split_line =[]
    split_line = line.split(" ")
    ip = split_line[0]
    time = split_line[3].strip("[]")
    return(ip,time)

with open ("day_07\\access.log","r",encoding="utf-8",errors="ignore") as f:
    for line in f:
            if "/admin" in line:
                attacker_ip,time_of_attack = extract_ip_time(line)
                print(f"The attacker {attacker_ip} access the admin page at {time_of_attack}")

        