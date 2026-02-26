# Day 11: The Scalpel (Advanced String Splitting & Joining)

I have already used `.split(" ")` in small ways. Today, I would practice more of it and learn its opposite: `.join()`.

Logs rarely use simple spaces. Real evidence comes separated by commas, pipes (`|`), tabs, colons, and mixed delimiters. If I want to parse artifacts cleanly and build readable reports, I must know how to break strings apart and stitch them back together.

---

## Core Concepts

### 1) `.split(delimiter)`
Breaks a string into a **list**, cutting it wherever the delimiter is found.

Example:

```python
"IP:192.168.1.5".split(":")
````

### 2) `.join(list)`

Takes a **list of strings** and glues them together using a chosen separator.

Example:

```python
"-".join(["A", "B", "C"])
```

---

## The Tasks: The Log Surgeon

Create `day_11/parsing.py`.

---

## Drill 11.1: The Custom Delimiter

**Goal:** Parse a syslog-style or colon-separated artifact.

### Code

1. Create the artifact:

```python
mac_address = "00:1A:2B:3C:4D:5E"
```

2. Split the MAC address into a list using the colon (`:`) as the delimiter.

3. Print the resulting list.

4. Print the **very last octet** using negative indexing.

---

## Drill 11.2: The Reassembly (`.join()`)

**Goal:** Convert a parsed list back into a clean string for a report.

### Code

1. Create the list:

```python
evidence_parts = ["Suspicious", "Executable", "Found", "cmd.exe"]
```

2. Use `.join()` to combine them with a dash (`-`) between each item.

**Syntax:**

```python
delimiter.join(list)
```

3. Example:

```python
report_line = "-".join(evidence_parts)
```

4. Print `report_line`.

---

## Drill 11.3: The Dual Parse (Real-World Scenario)

**Goal:** Extract a specific value hidden inside complex formatting.

### Code

1. Create the log entry:

```python
log_entry = "USER:admin|IP:192.168.1.50|ACTION:login"
```

2. First, split by the pipe (`|`) to get the three separate fields.

3. Grab the IP field. It will be index `1`:

```python
"IP:192.168.1.50"
```

4. Split that field again, this time using the colon (`:`), to isolate the raw IP address.

5. Print the raw IP address.

---

## The “Muscle Memory” Gauntlet (The Domain Extractor)

### The Mission

I have a list of email addresses. I need to extract just the domain names, remove duplicates, and print them as a single comma-separated string.

### Logic Flow

1. Create the list:

```python
emails = ["admin@evil.com", "user@corp.local", "ceo@evil.com", "it@corp.local"]
```

2. Create an empty list:

```python
unique_domains = []
```

3. Loop through the emails.

4. Split each email using `@`. The domain is the second part.

5. Check whether the domain is already in `unique_domains`.

* If not, append it.

6. Outside the loop, use `", ".join()` to format the final list into a single string.

7. Print the final string.

