import csv

#Task 15.1: The Basic Reader (csv.reader)

with open ("firewall_log.csv","r",encoding="utf-8",errors="ignore") as f:
    reader = csv.reader(f)
    for line in reader :
        print(line)

#Task 15.2: The Smart Reader (csv.DictReader)
with open ("firewall_log.csv","r",encoding="utf-8",errors="ignore") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(f"Source: {line['Source_IP']} -> Dest: {line['Destination_IP']} | Action: {line['Action']}")

#Task 15.3: The Filter & Count (DictReader + Logic)

denied_count = 0
with open ("firewall_log.csv","r",encoding="utf-8",errors="ignore") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Action'] == "DENY":
            denied_count += 1
            print(f"The Source: {row['Source_IP']} and The Destination: {row['Destination_IP']}")
    print(f"Total Denied connections: {denied_count}")

#Task 15.4: The Report Writer (csv.writer)
deny_list = []
with open ("firewall_log.csv","r",encoding="utf-8",errors="ignore") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Action"] == 'DENY':
            deny_list.append(row)

with open ("denied_traffic.csv","w",encoding="utf-8",errors="ignore") as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Source_IP", "Destination_IP", "Port"])
    for row in deny_list:
        writer.writerow([row['Timestamp'],row['Source_IP'],row['Destination_IP'],row['Port']])


#Task :The "Muscle Memory" Gauntlet (The Firewall Analyzer)
deny_summary = {}
deny_count = 0
with open ("firewall_log.csv","r",encoding="utf-8",errors="ignore") as f:
    reader = csv.DictReader(f)
    for row in reader:
        source_ip = row["Source_IP"]
        if row['Action'] == "DENY":
            if source_ip in deny_summary:
                deny_summary[source_ip] +=1
            else:
                deny_summary[source_ip] = 1

print(deny_summary)
with open ("deny_summary.csv","w",encoding="utf-8",errors="ignore") as f:
    writer = csv.writer(f)
    writer.writerow(["Source_IP","Deny_Count"])
    #for item in deny_summary.items(): --> This also works but not good for readablity 
        #writer.writerow(item)
    for ip,count in deny_summary.items():    
        writer.writerow([ip,count])