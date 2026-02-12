#The "Muscle Memory" Gauntlet (Assessment)
file_path = "day_07\\access.log"
ip_list =[]

with open(file_path,"r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        if "/admin" in line:
            temp_ip_list = line.split(" ")
            ip = temp_ip_list[0]
            if ip not in ip_list:
                ip_list.append(ip)
            

for i in ip_list:
    print(f"ALERT: IP {i} accessed Admin Panel")


with open("day_07\\supicious_activity.txt","w",encoding="utf-8",errors="ignore") as f:
    for i in ip_list:
        f.write(f"ALERT: IP {i} accessed Admin Panel at \n")
        

#The Task: The "Admin Hunter" Script

ip_list =[]

with open(file_path,"r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        if "/admin" in line:
            temp_ip_list = line.split(" ")
            ip = temp_ip_list[0]
            time = temp_ip_list[3].strip("[]")
            ip_list.append((ip,time))

#for i,t in ip_list:
 #   print(f"ALERT: IP {i} accessed Admin Panel at {t} ")

with open("day_07\\supicious_activity.txt","w",encoding="utf-8",errors="ignore") as f:
    for i,t in ip_list:
        f.write(f"ALERT: IP {i} accessed Admin Panel at {t} \n")

