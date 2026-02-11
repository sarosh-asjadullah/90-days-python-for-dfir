#TASK 6.1 The Reader (Ingesting Evidence)

with open (".\suspicious_ips.txt","r") as f:
    for line in f:
        print(f"Read IP: {line}")

#TASK 6.2 The Cleaner (Stripping WhiteSpace)

with open(".\suspicious_ips.txt","r") as f:
    for line in f:
        line = line.strip()
        print(f"Read IP: {line}")


#TASK 6.3: The Reporter (Writing Evidence)

bad_ips = ["10.0.0.50", "172.16.8.8"]
with open("report.txt","w") as f:
    for ip in bad_ips:
        f.write(f"Flagged: {ip}\n")


#TASK : The Muscle Memory Gauntlet
backup_ip = []
with open(".\suspicious_ips.txt", "r", encoding="utf-8",errors="ignore") as f:
    for line in f:
        backup_ip.append(line)
    
with open("backup_ips.txt","w",encoding="utf-8",errors="ignore") as f:
    for ip in backup_ip:
        f.write(ip)
