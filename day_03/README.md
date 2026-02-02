Welcome to **Day 3**.

[**Day 2**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_02) was about surgery (slicing strings). Today is about **decision making**.

In DFIR, We can't manually look at 10,000 log lines. We write a script to look for We. We tell the script: *"If the IP is from this country, alert me. If the file size is huge, flag it. Otherwise, ignore it."*

This is **Control Flow**.

### Core Concept: The Fork in the Road

Python executes code top-to-bottom, line-by-line. An `if` statement creates a branch.

1. **`if`**: The start of the question.
2. **`elif`**: (Else If) Try this if the previous one failed.
3. **`else`**: The catch-all. If nothing else was true, do this.
4. **Indentation:** Python uses **4 spaces** to know what code belongs inside the `if` block. If We mess up the indentation, the code breaks.

---

### The Tasks: The Logic Drills

Create a file: `day_03/logic_drills.py`.

#### Drill 3.1: The Port Sentry (Basic Equality)

* **Goal:** Check specific values using `==` (is equal to).
* **Code:**
1. `destination_port = 22`
2. Write an `if` statement: If `destination_port` is equal to **22**, print `"SSH traffic detected"`.
3. Write an `else` statement: Print `"Unknown traffic"`.
4. *Muscle Memory:* Change the variable to `80`, run it. Change it back to `22`.



#### Drill 3.2: The Severity Triage (Multiple Options)

* **Goal:** Using `elif` for multiple categories.
* **Code:**
1. `score = 85` (Simulating a risk score).
2. If `score` is greater than (`>`) 90: print `"Risk: CRITICAL"`.
3. `elif` `score` is greater than 75: print `"Risk: HIGH"`.
4. `else`: print `"Risk: LOW"`.



#### Drill 3.3: The Keyword Hunter (The `in` Operator)

* **Goal:** This is the **most important** operator for We. It checks if a substring exists inside a longer string.
* **Code:**
1. `log_line = "Failed password for invalid user admin from 192.168.1.1 port 55512 ssh2"`
2. If `"Failed password"` is **in** `log_line`:
* print `"ALERT: Brute Force Attempt"`


3. Else:
* print `"Log Normal"`





#### Drill 3.4: The "Kill Chain" (Compound Logic)

* **Goal:** Using `and` to require TWO things to be true.
* **Code:**
1. `file_extension = ".exe"`
2. `file_origin = "email_attachment"`
3. If `file_extension == ".exe"` **and** `file_origin == "email_attachment"`:
* print `"BLOCKED: Executable from email"`


4. Else:
* print `"File allowed"`





---

### The Muscle Memory Gauntlet

**Do not skip this.** To wire Wer brain, We must repeat the syntax until Wer fingers do it automatically.

1. **The "Not" Drill:**
* Write a check: `if status != "Clean":` (If status is **NOT** clean).
* Print `"Investigate"`.


2. **The "Or" Drill:**
* Write a check: `if port == 80 or port == 443:`
* Print `"Web Traffic"`.


3. **The Nested Drill:**
* Write an `if` inside an `if`:
```python
if "error" in log:
    if "critical" in log:
        print("Wake up the analyst!")

```



