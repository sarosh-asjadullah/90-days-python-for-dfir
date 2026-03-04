# Day 12: The Sorter (Lists vs. Tuples vs. Sets)

Until now, I have relied almost entirely on the **List** (`[]`). Today I learn the other two core data structures: the **Tuple** and the **Set**.

In DFIR, I choose data structures for tactical advantage:

- **List `[]`**: Ordered, mutable (can be changed). Best for chronological logs and sequences I need to edit.
- **Tuple `()`**: Ordered, immutable (locked). Best for fixed evidence pairs (e.g., IP + Port).
- **Set `{}`**: Unordered, strictly unique. The fastest way to deduplicate data or check if an IOC exists.

---

## The Tasks: Data Structure Drills

Create `day_12/structures.py`.

---

## Drill 12.1: The Locked Evidence (Tuple)

**Goal:** Understand immutability. Once a tuple is created, it cannot be altered.

### Code

1) Create a tuple representing a network connection:

```python
connection = ("192.168.1.50", 443)
````

2. Access it like a list:

```python
print(f"Target Port: {connection[1]}")
```

3. The Crash Test:

Try to change the port:

```python
connection[1] = 80
```

Run the script and observe the `TypeError`.
After observing the crash, comment out that line.

---

## Drill 12.2: The Instant Deduplicator (Set)

**Goal:** Use a set to instantly remove duplicates without writing a loop.

### Code

1. Create raw data:

```python
raw_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.5", "10.0.0.2"]
```

2. Convert list to set:

```python
unique_ips = set(raw_ips)
```

3. Print `unique_ips`. Notice duplicates are gone.

4. Convert it back to a list so it can be sorted:

```python
clean_list = list(unique_ips)
```

---

## Drill 12.3: The Venn Diagram (Set Operations)

**Goal:** Find overlapping IOCs between two threat intel feeds. Sets do this mathematically in one line.

### Code

1. Create two feeds:

```python
feed_a = {"1.1.1.1", "8.8.8.8", "10.10.10.10"}
feed_b = {"8.8.8.8", "9.9.9.9", "1.1.1.1"}
```

2. Find overlap using intersection (`&`):

```python
matches = feed_a & feed_b
```

3. Print `matches`.

---

## The “Muscle Memory” Gauntlet (The Triage Filter)

### The Mission

I have a list of all IPs that hit the firewall, and a separate list of known safe internal IPs. I need to print only the external (potentially hostile) IPs.

### Logic Flow

1. Create the inputs:

```python
traffic_log = ["192.168.1.1", "10.10.5.5", "8.8.8.8", "192.168.1.1", "45.33.22.11"]
safe_ips = ["192.168.1.1", "10.10.5.5"]
```

2. Convert both lists to sets.

3. Subtract the safe IPs from the traffic log using difference (`-`).

**Syntax:**

```python
hostile_set = set_a - set_b
```

4. Print the resulting set of hostile IPs.

