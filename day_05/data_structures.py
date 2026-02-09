
#Task 5.1: The Filter & Append (Crucial Skill)

raw_ip = ["192.168.1.1", "10.0.0.5", "172.16.8.8", "192.168.1.50"]
internal_ip = []

for ip in raw_ip:
    if "192.168" in ip:
        internal_ip.append(ip)

print(f"Internal IPs found: {internal_ip}")

#Task 5.2: The Protocol Map (Dictionary Basics)

protocol ={
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP"
}

print(f"Port 80 is {protocol[80]}")

#print(f"The value of port 9999 is {protocol[9999]}")

#Task 5.3: The Automated Lookup (Loop + Dict)

scanned_ports = [80,22,443,5565]

for port in scanned_ports:
    if port in protocol:
        print(f"The port {port} is : {protocol[port]}")
    else:
        print(f"The port {port} is : Unkown port")


#TASK : MALWARE HUNTER

files = ["cmd.exe", "pic.jpg", "run.exe", "data.db"]
executable = []

for file in files:
    if ".exe" in file:
        executable.append(file)
    
print(f"The list of executable found in the files are : {executable}")

#TASK : User Check 

users = {"admin": "Admin Access", "guest": "Guest Access"}
user_list =["guest","admin","root"]

for user in user_list:
    if user in users:
        print(f"The {user} has {users[user]}")
    else:
        print(f"There is no {user} user")
