# Day 7: The First Milestone (The Log Parser)

Today is a capstone day. I am not learning a new concept. I am combining Day 1 through Day 6 to build my first real tool.

## The Mission

I have been given a raw web server log. The goal is simple: extract a list of every IP address that attempted to access the sensitive `/admin` paths.

## The Setup

Create a file named `day_07/access.log` and paste the following data inside:

```text
192.168.1.10 - - [10/Oct/2023:13:55:36] "GET /index.html HTTP/1.1" 200 2326
10.0.0.5 - - [10/Oct/2023:13:55:38] "POST /admin/login.php HTTP/1.1" 401 532
172.16.0.1 - - [10/Oct/2023:13:55:40] "GET /images/logo.png HTTP/1.1" 200 5032
192.168.1.10 - - [10/Oct/2023:13:56:01] "GET /about.html HTTP/1.1" 200 4123
10.0.0.5 - - [10/Oct/2023:13:56:10] "POST /admin/dashboard HTTP/1.1" 403 211
```
## The Task: The “Admin Hunter” Script

Create `day_07/admin_hunter.py`.

---

## Step 1: The Plan (Logic Flow)

Before coding, read this flow. This is the logic I should be able to explain out loud:

1) Open `access.log` for reading.  
2) Open `suspicious_activity.txt` for writing.  
3) Loop through every line of the log.  
4) Check: Does the line contain `"/admin"`?  
5) If **Yes**:  
   - Split the line and extract the IP address (it is the first token).  
   - Write the IP and timestamp to the report in a clean format.  
6) If **No**: Ignore it.

**Hint for splitting:** `parts = line.split(" ")` → IP is `parts[0]`  
**Hint for output:** Make it look professional, e.g. `ALERT: IP <ip> accessed Admin Panel`

---

## Step 2: The Execution

Write the script.

---

## The “Muscle Memory” Gauntlet (Assessment)

This is the first exam. Same task, but with one logic twist.

### The Twist: Only Unique IPs

The attacker `10.0.0.5` is noisy. I do not want the same IP listed 50 times.

**Requirement:** Only write **unique** IPs to the report.

### How

1) Create a list: `seen_ips = []`  
2) Before writing, check: `if ip not in seen_ips:`  
3) If it is new: write it and append it to `seen_ips`.
