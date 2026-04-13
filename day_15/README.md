Welcome to **Day 15**.

In [**Day 14**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_14), I built my second milestone — a complete CLI Log Analyzer combining functions, error handling, file I/O, sets, and sys.argv into one modular tool. Today, I move from raw text parsing to **structured data**.

Until now, every file I parsed was raw text — I split by spaces and hoped the format stayed consistent. Real forensic exports are rarely that forgiving. KAPE module outputs, Splunk exports, timeline CSVs from log2timeline — these all come as structured CSV files with headers, commas inside quoted fields, and edge cases that would break a naive `.split(",")`. Today I learn to use Python's built-in `csv` module, which handles all of that automatically. Think of it as upgrading from a hand saw to a table saw — same job, but the `csv` module keeps the cuts straight even when the wood is warped.

### Core Concepts

- **`csv.reader`**: Reads a CSV file row by row. Each row comes back as a list.
- **`csv.DictReader`**: Reads a CSV file row by row. Each row comes back as a dictionary where the keys are the column headers. This is the one I will use most in DFIR because I can access fields by name instead of index number.
- **`csv.writer`**: Writes lists to a CSV file.
- **`csv.DictWriter`**: Writes dictionaries to a CSV file with headers.

---

### The Setup

Before starting the code, I created a dummy file in my `day_15` folder named `firewall_log.csv` with this content:

```
Timestamp,Source_IP,Destination_IP,Port,Action
2024-03-15 08:10:01,192.168.1.50,10.0.0.5,443,ALLOW
2024-03-15 08:10:05,10.0.0.5,192.168.1.50,80,ALLOW
2024-03-15 08:11:30,172.16.0.1,8.8.8.8,53,ALLOW
2024-03-15 08:12:00,192.168.1.50,45.33.22.11,443,DENY
2024-03-15 08:12:45,10.0.0.5,185.199.108.153,443,DENY
2024-03-15 08:13:10,192.168.1.50,45.33.22.11,80,DENY
```

---

### The Tasks: Structured Data Mastery

I created `day_15/csv_drills.py`.

#### Task 15.1: The Basic Reader (`csv.reader`)

Goal: Read the CSV row by row as lists.

1. Import `csv`.
2. Open `firewall_log.csv` for reading.
3. Create a reader object: `reader = csv.reader(file)`.
4. Loop through `reader` and print each row.
5. Observe: each row is a list like `['2024-03-15 08:10:01', '192.168.1.50', '10.0.0.5', '443', 'ALLOW']`.

#### Task 15.2: The Smart Reader (`csv.DictReader`)

Goal: Access fields by column name instead of index number.

1. Import `csv`.
2. Open `firewall_log.csv` for reading.
3. Create a reader object: `reader = csv.DictReader(file)`.
4. Loop through `reader`.
5. Print: `f"Source: {row['Source_IP']} -> Dest: {row['Destination_IP']} | Action: {row['Action']}"`.

I do not need to remember that Source_IP is index 1. I just ask for it by name.

#### Task 15.3: The Filter & Count (DictReader + Logic)

Goal: Combine CSV reading with the filtering logic I already know.

1. Open `firewall_log.csv` with `DictReader`.
2. Create a counter `denied_count = 0`.
3. Loop through rows. If `row['Action']` equals `"DENY"`, increment the counter and print the row's Source_IP and Destination_IP.
4. After the loop, print: `f"Total denied connections: {denied_count}"`.

#### Task 15.4: The Report Writer (`csv.writer`)

Goal: Save my filtered results into a new CSV file.

1. First, read `firewall_log.csv` and collect all rows where `Action` is `"DENY"` into a list.
2. Open a new file `denied_traffic.csv` in write mode.
3. Create a writer object: `writer = csv.writer(file)`.
4. Write the header row first: `writer.writerow(["Timestamp", "Source_IP", "Destination_IP", "Port"])`.
5. Loop through the denied rows and write each one using `writer.writerow()`.

---

### The "Muscle Memory" Gauntlet (The Firewall Analyzer)

**The Mission:** I built a script that reads the firewall CSV, groups denied connections by Source IP, and writes a summary report.

1. Open `firewall_log.csv` with `DictReader`.
2. Create an empty dictionary: `deny_summary = {}`.
3. Loop through rows. If the action is `"DENY"`:
   - If the Source_IP is already a key in `deny_summary`, increment its value by 1.
   - If it is not, add it with a value of 1.
4. After the loop, print each IP and its deny count.
5. Write the summary to `deny_summary.csv` with headers `Source_IP,Deny_Count`.

This dictionary-as-counter pattern is something I will use constantly when analyzing logs at scale.