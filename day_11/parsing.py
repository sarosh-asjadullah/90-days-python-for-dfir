#TASK 11.1: The Custom Delimiter
print("\nTASK 11.1: The Custom Delimiter")
mac_address = "00:1A:2B:3C:4D:5E"
split_mac = mac_address.split(":")
print(split_mac)
last_octet = "".join(split_mac[-2:])

print(last_octet)


#TASK 11.2: The Reassembly (.join())
print("\n#TASK 11.2: The Reassembly (.join())")

evidence_parts = ["Suspicious", "Executable", "Found", "cmd.exe"]
report_line = "-".join(evidence_parts)
print(report_line)



#TASK 11.3: The Dual Parse (Real-World Scenario)
print("\nTASK 11.3: The Dual Parse (Real-World Scenario)")

log_entry = "USER:admin|IP:192.168.1.50|ACTION:login"
log_split = log_entry.split("|")
ip_split = log_split[1].split(":")
print(ip_split[1])

#TASK:The "Muscle Memory" Gauntlet (The Domain Extractor)
print('\nThe "Muscle Memory" Gauntlet (The Domain Extractor)')
emails = ["admin@evil.com", "user@corp.local", "ceo@evil.com", "it@corp.local"]
unique_domain = []
for email in emails:
    unique_domain.append(email.split("@"))
print(unique_domain)
final_domain_list=[]
for i in range(len(unique_domain)):
    if unique_domain[i][1] not in final_domain_list:
        final_domain_list.append(unique_domain[i][1])


final_domain_list = ", ".join(final_domain_list)
print(final_domain_list)

#The above one  is my initial attempt answer but better answer is below 
emails = ["admin@evil.com", "user@corp.local", "ceo@evil.com", "it@corp.local"]
unique_domains = []

for email in emails:
    domain = email.split("@")[1]
    if domain not in unique_domains:
        unique_domains.append(domain)

final_string = ", ".join(unique_domains)
print(final_string)