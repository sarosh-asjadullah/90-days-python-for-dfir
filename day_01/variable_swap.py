# Day 1 - Task 1.2
# Goal: Understand how variables hold and change data in memory.

primary_dns = "8.8.8.8"
secondary_dns = "1.1.1.1"

print("Initial DNS Settings:")
print(f"Primary: {primary_dns}")
print(f"Secondary: {secondary_dns}")

# Re-assigning the variables (Simulating a configuration change)
primary_dns = "9.9.9.9"
secondary_dns = "8.8.4.4"

print("\nUpdated DNS Settings:")
print(f"Primary: {primary_dns}")
print(f"Secondary: {secondary_dns}")
