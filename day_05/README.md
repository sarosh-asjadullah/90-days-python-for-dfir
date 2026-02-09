
## Day 5: The Collector (List Building & Dictionaries)

Yesterday I pulled data out of lists. Today I start building them.

In investigations, you rarely begin with a clean list. You start empty, then you add evidence as you discover it. In Python, that habit becomes `append()`.

Today also introduces the **Dictionary**: the structure that makes analysts fast. A dictionary is how you connect one thing to another, like `IP -> Owner`, `Port -> Service`, or `Hash -> Verdict`.

### Core Concepts

#### 1) Appending
Start with an empty list and add items as you go.

- `internal_ips = []`
- `internal_ips.append(ip)`

#### 2) The Dictionary
Key-value mapping.

- `{"Key": "Value"}`

#### 3) Lookup
If you know the key, you can retrieve the value instantly.

---

### The Task: The Evidence Collector

Create `day_05/data_structures.py`.



#### Drill 5.1: The Filter & Append (Crucial Skill)

**Goal:** Separate internal traffic into a clean list you can trust.

#### Code

1) Create the raw list:

```python
raw_ips = ["192.168.1.1", "10.0.0.5", "172.16.8.8", "192.168.1.50"]
````

2. Create an empty list:

```python
internal_ips = []
```

3. Loop through `raw_ips`.

4. Inside the loop:

* If the IP starts with `"192.168"`, append it to the new list.

5. Outside the loop, print:

```python
print(f"Internal IPs found: {internal_ips}")
```

---

#### Drill 5.2: The Protocol Map (Dictionary Basics)

**Goal:** Convert raw numbers into meaning using a dictionary.

#### Code

1. Create the dictionary:

```python
protocols = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP"
}
```

2. Access a value:

```python
print(f"Port 80 is {protocols[80]}")
```

3. Challenge (intentional crash):

Try printing a port that is not in the dictionary:

```python
print(protocols[9999])
```

Observe: it will crash with a `KeyError`. I want that to happen once so I remember why safe lookups matter.

---

#### Drill 5.3: The Automated Lookup (Loop + Dict)

**Goal:** Take scan output and translate it automatically.

#### Code

1. Use the `protocols` dictionary from Drill 5.2.

2. Create the list of open ports:

```python
scanned_ports = [80, 22, 443]
```

3. Loop through `scanned_ports`.

4. Inside the loop:

* If the port is in `protocols`, print its name.
* Else, print `Unknown`.

Example structure:

```python
for port in scanned_ports:
    if port in protocols:
        print(f"Port {port} is {protocols[port]}")
    else:
        print(f"Port {port} is Unknown")
```

---

### The “Muscle Memory” Repetition

This is a core scripting pattern: **Loop + Condition + Append**. Drill it until it becomes automatic.

#### 1) The “Malware Hunter”

**Goal:** Build a list of executables from mixed file types.

```python
files = ["cmd.exe", "pic.jpg", "run.exe", "data.db"]
executables = []

for f in files:
    if f.endswith(".exe"):
        executables.append(f)

print(f"Executables found: {executables}")
```

#### 2) The “User Check”

**Goal:** Check whether a key exists before assuming it does.

```python
users = {"admin": "Admin Access", "guest": "Guest Access"}

print("root" in users)   # False
print("admin" in users)  # True
```
=
