import json

#Task 16.1: The Loader (Reading JSON)

with open ("alert.json","r",encoding="utf-8",errors="ignore") as f:
    data = json.load(f)
    
print(data)
print(type(data))

#Task 16.2: The Deep Dive (Accessing Nested Data)
print(data["alert_id"])
print(data["source"]["ip"])
print(data["destination"]["country"])
for ioc in data["indicators"]:
    print(ioc) 

#Task 16.3: The Filter (Processing a JSON Array)

with open("multi_alerts.json", "r", encoding="utf-8", errors="ignore") as f:
    data = json.load(f)

# If data is a list of dictionaries (standard for JSON arrays)
for alert in data:
    # Use .get() to safely check the "severity" key
    if alert.get("severity") in ["HIGH", "CRITICAL"]:
        print(f"Alert ID: {alert['alert_id']}, Source IP: {alert['source_ip']}")

blocked_data =[]
for alert in data:
    if alert.get("action") == 'blocked':
        print(alert)
        blocked_data.append(alert)

with open ("blocked_alerts.json","w",encoding="utf-8",errors="ignore") as f:
    json.dump(blocked_data,f,indent=4)

#Task: The Muscle Memory Gauntlet (Alert Summarizer)
import json

# Open the multi-alert JSON file and load it into a Python list of dictionaries
with open("multi_alerts.json", "r", encoding="utf-8", errors="ignore") as f:
    data = json.load(f)

# Empty dictionary — this will dynamically build itself as we encounter severity levels
# We do NOT need to pre-define keys like "HIGH", "CRITICAL", "LOW"
# The loop below will create them on first encounter and increment on repeat encounters
severity_counts = {}

# Empty list to collect destination IPs of blocked connections
blocked_ips = []

# Single loop through the entire data list
# Each "alert" is one dictionary from the JSON array
for alert in data:

    # --- Severity Counting (Dictionary-as-Counter Pattern) ---
    # Grab the severity value from this alert (e.g., "HIGH", "CRITICAL", "LOW")
    sev = alert["severity"]

    # Check: have I seen this severity before in my dictionary?
    if sev in severity_counts:
        # Yes — this key already exists, so I increment its count by 1
        severity_counts[sev] += 1
    else:
        # No — first time seeing this severity, so I create the key and set count to 1
        severity_counts[sev] = 1

    # --- Blocked IP Collection ---
    # If this alert was blocked, grab the destination IP for the report
    if alert["action"] == "blocked":
        blocked_ips.append(alert["dest_ip"])

# Build the final summary dictionary
# len(data) gives total alert count — no need to manually count with a variable
# set() removes duplicate IPs, sorted() puts them in order, list() converts back from set
summary = {
    "total_alerts": len(data),
    "severity_breakdown": severity_counts,
    "blocked_ips": sorted(set(blocked_ips))
}

# Write the summary to a new JSON file with indent=4 for human-readable formatting
with open("summary.json", "w", encoding="utf-8", errors="ignore") as f:
    json.dump(summary, f, indent=4)