# Day 1 - Task 1.1
# Goal: Use input() to capture data and print() to format a report.

print("--- Incident Triage Intake ---")

# Capturing evidence/metadata
analyst_name = input("Enter Analyst Name: ")
case_number = input("Enter Case Number: ")
target_ip = input("Enter Target IP Address: ")

# Outputting the formatted report
# Note: the 'f' before the quotes allows us to put variables directly inside {}
print(f"\n[REPORT] Analyst: {analyst_name} | Case: {case_number} | Target: {target_ip}")
