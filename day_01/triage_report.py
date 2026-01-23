analyst_name:str = input("\nEnter the analyst name: ").strip()
case_number:str = input("\nEnter the Case number: ").strip()
ip_address:str = input("\nEnter the target ip address: ").strip()

output = f"[REPORT] Analyst: {analyst_name} | Case: {case_number} | Target:{ip_address}"
print(output)
