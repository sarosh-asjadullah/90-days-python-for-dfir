#TASK 17.1  — Verify the Auto-Close Behavior

with open ("firewall_log.txt","r",encoding="utf",errors="ignore") as f:
    for lines in f:
        print(lines)
print(f.closed)

#TASK 17.2 — The Dual Context Manager (Read + Write)
with open ("raw_alerts.txt","r") as infile, open("critical_only.txt","w") as outfile:
    for line in infile:
        if "CRITICAL" in line:
            outfile.write(line)

#TASK 17.3 — Append vs Overwrite Under a Context Manager
alert_log_path = "running_alerts.txt"
with open (alert_log_path,'w') as writefile:
    writefile.write("Session started\n")

with open(alert_log_path,"a") as appendfile:
    appendfile.write("Alert: 192.168.1.5 - port scan detected\n")

with open(alert_log_path,"a") as appendfile:

    appendfile.write("Alert: 10.0.0.2 - lateral movement\n")

with open(alert_log_path,"r") as readfile:
    for line in readfile:
        print(line)

#the file doesnt grow because the first one is w mode and this creates the file after discarding what was already inside it

#TASK 17.4 — Wrapping a Context Manager in a Function

def extract_errors (input_path,output_path):
    count = 0
    with open (input_path,"r") as readfile, open (output_path,"w") as writefile :
        for line in readfile:
            if "ERROR" in line :
                count +=1
                writefile.write(line)
    return count,output_path
 

count_error = extract_errors("system_log.txt","errors_only.txt")
print(f"Processed evidence: {count_error[0]} errors extracted to {count_error[1]}")


#TASK Muscle Memory Gauntlet: The Evidence Filter Pipeline
with open('ids_export.txt','w') as writefile:
    writefile.write("2026-04-16T08:01:05Z LOW Reconnaissance probe from 10.10.10.99 - port 80\n"
"2026-04-16T08:03:17Z HIGH Brute force attempt on RDP from 185.220.101[.]47 - 52 failures\n"
"2026-04-16T08:05:44Z MEDIUM Unusual outbound DNS query volume from DIRTY_PC\n"
"2026-04-16T08:07:29Z CRITICAL Mimikatz execution detected on 10.10.10.45 - lsass access confirmed\n"
"2026-04-16T08:09:11Z LOW ICMP sweep detected from 10.10.10.20\n"
"2026-04-16T08:11:58Z HIGH Lateral movement via SMB: 10.10.10.45 -> 10.10.10.30\n"
"2026-04-16T08:14:33Z MEDIUM Failed Kerberos pre-authentication for user svc_backup\n"
"2026-04-16T08:16:47Z CRITICAL Ransomware signature matched on 10.10.10.55 - vssadmin delete shadows\n"
"2026-04-16T08:19:02Z LOW ARP scan detected on subnet 10.10.10.0/24\n"
"2026-04-16T08:21:39Z HIGH Suspicious PowerShell encoded command executed on DC1\n"
"2026-04-16T08:23:14Z MEDIUM Outbound HTTP POST to uncategorized domain from 10.10.10.33\n"
"2026-04-16T08:25:50Z CRITICAL Pass-the-hash attack detected: NTLM relay from 10.10.10.45\n")
    
def filter_high_severity (input_path,output_path,summary_path):
    count = 0
    with open (input_path,"r") as readfile, open(output_path,'w') as writefile:
        for line in readfile:
            if "HIGH" in line or "CRITICAL" in line:
                writefile.write(line)
                count += 1
    with open(summary_path,"w") as writesummary:
       writesummary.write(f"Total high-severity events: {count}\n")
    return count

counter = filter_high_severity("ids_export.txt","filter_ids.txt","summary_ids.txt")
print(f"\nTotal high-severity events: {counter}\n")