# Day 9: The Shield (Error Handling)

In DFIR, data is dirty. Logs are truncated, files are locked, and permissions are denied.
If my script crashes on the 5th file out of 10,000, I lose hours of processing.

Today, I teach my script to survive.

---

## Core Concepts

### 1) `try`

The block of code that might crash.

### 2) `except`

The safety net. If the `try` block crashes, execution jumps here instead of dying.

### 3) Specific Errors

Catching a precise failure (e.g., `FileNotFoundError`) is better than catching everything blindly.

---

## The Tasks: Bulletproof Coding

Create `day_09/error_handling.py`.

---

## Drill 9.1: The Crash Test (Basic Syntax)

**Scenario:** I am calculating the ratio of malicious packets to total packets.

### Task

1. Create a function: `get_ratio(malicious, total)`
2. Inside, try to return `malicious / total`
3. Wrap it in a `try/except` block
4. If `ZeroDivisionError` occurs (because `total` is `0`):

   * return `0`
   * print `"Error: No data found."`

**Test:** Call `get_ratio(10, 0)`. It should not crash.

---

## Drill 9.2: The File Safeguard (Missing Evidence)

**Scenario:** I have a list of files to hash/read, but some might have been deleted.

### Task

1. Create:

```python
files = ["evidence.txt", "missing_file.txt"]
```

2. Loop through the list.
3. Inside the loop, start a `try` block:

   * `with open(filename, "r")` and read it
4. Add:

* `except FileNotFoundError:`

  * print `f"ALERT: {filename} is missing!"`

**Note:** Ensure `evidence.txt` exists (create it). Ensure `missing_file.txt` does not.

---

## Drill 9.3: The Generic Net (Catching Unknowns)

**Scenario:** I am parsing data that may be completely malformed.

### Task

1. Create:

```python
raw_data = ["192.168.1.1", 500, "10.0.0.1"]
```

2. Loop through `raw_data`.
3. Try to split the item:

* `parts = item.split(".")`

4. Handle failures:

* `except AttributeError:` (integers do not have `.split()`)

  * print `"Not a string, skipping."`

* `except Exception as e:` (catch-all)

  * print `f"Unknown Error: {e}"`

---

## The “Muscle Memory” Gauntlet

This is the standard pattern for high-volume log processing.

### The “Resilient Parser”

1. Create:

```python
logs = ["Entry 1", "Entry 2", 999, "Entry 3"]
```

2. Write a loop that prints the lowercase version of each entry.

**Constraint:** The loop MUST NOT CRASH when it hits `999`.

It must print:

* `"Error processing item: 999"`

…and then continue to `"Entry 3"`.
