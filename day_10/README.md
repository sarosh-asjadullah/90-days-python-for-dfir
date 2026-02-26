
# Day 10: The Scout (Working with Built-in Modules)

Phase 1 is almost over. I have learned the grammar of Python: variables, loops, conditions, files, and functions. Now I begin learning how to use the tools Python already brings with it.

In DFIR, I do not write code to read the hard drive from scratch. I use the `os` library. I do not calculate timestamps manually. I use the `time` library.

Today is about using built-in modules to interact with the operating system and time itself.

---

## Core Concepts

### 1) `import`
The command used to load a tool.

Example:

```python
import os
````

This loads Python’s operating system tools.

### 2) `os` Module

My bridge to the file system. It can:

* list files
* check whether a file exists
* get file sizes
* work with paths and directories

### 3) `time` Module

Critical for forensics and automation. It can:

* generate readable timestamps
* pause execution
* help mark scan start and end times

---

## The Tasks: The System Scout

Create `day_10/system_tools.py`.

---

## Drill 10.1: The Recon (Where am I?)

**Goal:** Orient myself in the file system.

### Code

1. Import the module:

```python
import os
```

2. Get the current working directory:

```python
cwd = os.getcwd()
```

3. Print it:

```python
print(f"Current Analysis Directory: {cwd}")
```

4. Get the list of files in that directory:

```python
files = os.listdir(cwd)
```

5. Print the result:

```python
print(f"Files found: {files}")
```

---

## Drill 10.2: The Evidence Validator

**Goal:** Check whether a file exists before trying to use it.

This is defensive coding. I should never assume the file is there.

### Code

1. Import the module:

```python
import os
```

2. Define a target file:

```python
target_file = "day_10/system_tools.py"
```

3. Check whether it exists:

```python
if os.path.exists(target_file):
```

4. If it exists, get its size:

```python
size = os.path.getsize(target_file)
print(f"Target found. Size: {size} bytes")
```

5. Otherwise:

```python
print("Target missing.")
```

---

## Drill 10.3: The Timestamp Generator

**Goal:** Mark the start and end of a scan.

### Code

1. Import the module:

```python
import time
```

2. Print the start time:

```python
print(f"Scan started at: {time.ctime()}")
```

3. Simulate work:

```python
time.sleep(2)
```

4. Print the end time:

```python
print(f"Scan finished at: {time.ctime()}")
```

---

## The “Muscle Memory” Gauntlet (The Directory Scanner)

This is a classic automation task.

### The Mission

Write a script that scans the current directory. It must find all Python files (`.py`) and print their name and size.

### Logic Flow

1. Import `os`
2. Loop through `os.listdir()`
3. Check:

```python
if file_name.endswith(".py"):
```

This introduces a new and useful string method: `.endswith()`.

4. Get the file size
5. Print a clean report:

```python
[SCRIPT] {name} | {size} bytes
```

### Example Structure

```python
import os

for file_name in os.listdir():
    if file_name.endswith(".py"):
        size = os.path.getsize(file_name)
        print(f"[SCRIPT] {file_name} | {size} bytes")
```

