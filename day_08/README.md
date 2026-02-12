# Day 8: The Modularizer (Introduction to Functions)

Welcome to Phase 1, Week 2. Until now, I have been writing “spaghetti code”: one long script that runs top to bottom. When I want to reuse logic (like IP extraction), I end up copying and pasting it into new places.

Today, I stop doing that. I wrap logic into **functions**.

---

## Core Concepts

### 1) `def`
The keyword used to define a function.

### 2) Parameters (Arguments)
Inputs passed into a function.

### 3) `return`
The output a function sends back to the caller.

### 4) Scope
Variables created inside a function die when the function ends. They do not exist outside it.

---

## The Task: The Toolsmith’s Kit

Create `day_08/functions.py`.

---

## Drill 8.1: The Sanitize Function

**Scenario:** I constantly need to strip whitespace and lower-case strings. I will stop rewriting this every time.

### Task

1) Define a function:

```python
def clean_artifact(artifact):
````

2. Inside, do the work:

* `cleaned = artifact.strip().lower()`

3. Send it back:

* `return cleaned`

4. Test it:

Call the function on `" Malware.EXE "` and print the result.

---

## Drill 8.2: The IOC Checker (Boolean Returns)

**Scenario:** A function that answers a Yes/No question.

### Task

1. Define:

```python
def is_critical_ip(ip_address):
```

2. Logic:

* If the IP starts with `"192.168"`, `return False` (internal/safe).
* Else, `return True` (external/potential threat).

3. Test it:

Loop through a list of IPs and print:

`f"Checking {ip}: Critical? {is_critical_ip(ip)}"`

---

## Drill 8.3: The Log Parser (Function with Multiple Returns)

**Scenario:** Extracting data should be its own tool.

### Task

1. Define:

```python
def parse_log_line(line):
```

2. Logic:

* Split the line by space.
* Extract the timestamp (index `3`) and IP (index `0`).
* Return them both: `return timestamp, ip`

3. Test it:

```python
sample = '10.0.0.5 - - [10/Oct/2023]'
time, ip = parse_log_line(sample)
print(f"Time: {time} | IP: {ip}")
```

---

## The “Muscle Memory” Gauntlet

Functions are about structure. The syntax must become automatic.

### The “Refactor”

Take your code from Day 7 (The Admin Hunter) and refactor it.

1. Create a function:

* `def extract_ip(line):` that takes a line and returns the IP.

2. Rewrite your main loop to use this function instead of doing split logic inside the loop.

Use this structure:

```python
def extract_ip(line):
    parts = line.split(" ")
    return parts[0]

# Main Code
with open("access.log", "r") as f:
    for line in f:
        if "/admin" in line:
            ip = extract_ip(line)  # Look how clean this is!
            print(ip)
```

