#Task 12.1: The Locked Evidence (Tuple)
print(f"\nTask 12.1: The Locked Evidence (Tuple)")
connection = ("192.168.1.50", 443)
print(connection)
try:
   connection[1] = input("Enter the new port:")
except TypeError:
    print(f"'tuple' object does not support item assignment")
    
print(f"Target Port: {connection[1]}")

#Task 12.2: The Instant Deduplicator (Set)
print("\nTask 12.2: The Instant Deduplicator (Set)")
raw_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.5", "10.0.0.2"]
unique_ips = set(raw_ips)
print(f"Printing raw data set containing duplicate value {raw_ips}")
print(f"Printing unique_ips using set function {unique_ips}")
clean_list = list(unique_ips)
print(f"Printing the clean data list {clean_list}")

#Task 12.3: The Venn Diagram (Set Operations)
print(f"\nTask 12.3:The Venn Diagram (Set Operations)")

feed_a = {"1.1.1.1", "8.8.8.8", "10.10.10.10"}
feed_b = {"8.8.8.8", "9.9.9.9", "1.1.1.1"}
matches = feed_a & feed_b # Find the overlap using the intersection operator (&)
matches1 = set.intersection(feed_a,feed_b)
print("Printing the feed_a ",feed_a)
print("Printing the feed_b ",feed_b)
print("Printing the match ",matches)
print(matches1)

#TASK The "Muscle Memory" Gauntlet (The Triage Filter)

traffic_log = ["192.168.1.1", "10.10.5.5", "8.8.8.8", "192.168.1.1", "45.33.22.11"]

safe_ips = ["192.168.1.1", "10.10.5.5"]



traffic_log_set = set(traffic_log)

safe_ip_set = set(safe_ips)

hostile_ip = traffic_log_set - safe_ip_set

print(f" These are the hostile_ip = {hostile_ip}")