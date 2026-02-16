#Drill 9.1: The Crash Test (Basic Syntax)

def get_ratio(malicious,total):
    try:
        return malicious/total
    except ZeroDivisionError:
        return 0
       

first_input = int(input("Enter Malicious Count: "))
second_input = int(input("Enter Total Count: "))

ratio = get_ratio(first_input,second_input)
if ratio == 0:
     print("Error:No data found.")
else:
    print(f"The ratio is : {ratio}")

print(50*"-")
#Drill 9.2: The File Safeguard (Missing Evidence)
files = ["evidence.txt", "missing_file.txt"]
for i in files:
    try:
        with open(i,"r",encoding="utf-8",errors="ignore") as f:
            for line in f:
                print((line).strip("\n"))
    except FileNotFoundError:
        print(f"ALERT: {i} is missing!")

print(50*"-")
#Drill 9.3: The Generic Net (Catching Unknowns)
raw_data = ["192.168.1.1", 500, "10.0.0.1"]
split_value = []
for i in raw_data:
    try:
        split_value.append(i.split("."))
    except AttributeError:
        print("Not a string, skipping.")
    except Exception as e:
        print(f"Unknown Error: {e}")
print(split_value)


print(50*"-")
#Task The "Muscle Memory" Gauntlet

logs = ["Entry 1", "Entry 2", 999, "Entry 3"]
for item in logs:
    try:
        print(item.lower())
    except AttributeError:
        print(f"Error processing item: {item}")


