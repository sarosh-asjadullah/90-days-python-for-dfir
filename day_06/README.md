# Day 6: The Investigator (File I/O)

Up until now, I have hard-coded my data (`ips = [...]`). Real forensics does not work like that. Evidence lives outside the script: logs, exports, config files, and text dumps.

Today is about **File I/O**: opening files, reading them safely, and writing out results. This is where scripts stop feeling like practice and start behaving like tools, because they interact with the operating system.

---

## Core Concepts

### 1) `open()` Function
Connects your script to a file on disk.

### 2) Modes
- `"r"`: Read (default). **Fails** if the file does not exist.
- `"w"`: Write. **DANGER:** overwrites the file completely.
- `"a"`: Append. Adds content to the end of the file.

### 3) The `with` Statement (Context Manager)
It automatically closes the file even if your script crashes.  
For investigations and automation, treat this as mandatory.

---

## The Setup

Before you write any code, create a file in `day_06/` named:

- `suspicious_ips.txt`

Paste this content into it exactly:

text
192.168.1.1
10.0.0.50
172.16.8.8
8.8.8.8


---

## The Task: The Evidence Handler

Create `day_06/file_drills.py`.

---

## Drill 6.1: The Reader (Ingesting Evidence)

**Goal:** Read a file line-by-line.

### Code

Use the `with open()` syntax.
Loop through the file object.
Print each line.

```python
with open("suspicious_ips.txt", "r") as f:
    for line in f:
        print(f"Read IP: {line}")
```

### Observation

You will notice extra blank lines in output.
Reason: each line already ends with `\n`, and `print()` adds another newline.

---

## Drill 6.2: The Cleaner (Stripping Whitespace)

**Goal:** Fix the newline issue from 6.1.

### Code

Repeat the loop, but clean each line before printing:

```python
with open("suspicious_ips.txt", "r") as f:
    for line in f:
        line = line.strip()
        print(f"Read IP: {line}")
```

---

## Drill 6.3: The Reporter (Writing Evidence)

**Goal:** Save analysis output into a report file.

### Code

1. Create flagged items:

```python
bad_ips = ["10.0.0.50", "172.16.8.8"]
```

2. Open a new file `report.txt` in write mode (`"w"`).
3. Loop through `bad_ips`.
4. Write each entry, and **manually add** a newline `\n`.

```python
with open("report.txt", "w") as f:
    for ip in bad_ips:
        f.write(f"FLAGGED: {ip}\n")
```

### Verification

Check your folder:

* Did `report.txt` appear?
* Open it and confirm the content is correct.

---

## The “Muscle Memory” Gauntlet

File I/O syntax is easy to forget if it is not drilled.

### The “Copy Cat”

**Goal:** Read from `suspicious_ips.txt` and write every line into `backup_ips.txt`.

Hint: Opening a write file inside the read loop is messy.

Better pattern:

1. Read everything into a list.
2. Write the list into a new file.

Use this structure:

```python
# Step 1: Read
lines = []
with open("suspicious_ips.txt", "r") as f:
    lines = f.readlines()

# Step 2: Write
with open("backup_ips.txt", "w") as f:
    for line in lines:
        f.write(line)
```


