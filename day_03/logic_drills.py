#Task 3.1: The Port Sentry (Basic Equality)

destination_port = 80
if destination_port == 22:
    print("SSH Traffic detected")
else:
    print("Unknown Traffic")

#Task 3.2: The Severity Triage (Multiple Options)
score = 91
if score > 90:
    print("Risk:Critical")
elif score > 75:
    print("Risk:High")
else:
    print("Risk:Low")

#Task 3.3: The Keyword Hunter (The in Operator)

log_line = "Failed password for invalid user admin from 192.168.1.1 port 55512 ssh2"
if "Failed password" in log_line:
    print("Alert: Brute Force Attempt")
else:
    print("Log Normal")

#Task 3.4  The "Kill Chain" (Compound Logic)
file_extension = ".exe"
file_origin = "email_attachment"
if file_extension == ".exe" and file_origin == "email_attachment":
    print("Blocked : Executable from Email")
else:
    print("File Allowed")


#EXTRA TASK
#NOT DRILL
status = "Clean"
if status != "Clean":
    print("Investigate")

#OR Drill

port = 25

if port == 443 or destination_port == 80:
    print("Web traffic")

#Nested Drill

if "Failed" in log_line:
    if "admin" in log_line:
        print("Wake up the Analyst!")