Welcome to **Day 17**.

In [**Day 16**](../day_16/), I worked with JSON data — loading structured alert logs, parsing nested fields, and writing filtered summaries back to disk. Today, I am learning what actually happens when Python opens and closes a file, and why the `with` statement is the only correct way to handle files in production DFIR scripts.

In DFIR, I work with evidence files that must not be corrupted, left open, or partially written. If a script crashes halfway through writing a report and the file handle was never closed, the output file is incomplete and potentially locked by the process. The `with` statement prevents this by guaranteeing cleanup — it is like a hotel room door that locks itself automatically when I walk out. Without it, I have to remember to lock the door myself, and at 3 AM during a live incident, I will forget.

### Core Concept

When Python enters a `with open(...)` block, it calls `__enter__` on the file object — this opens the file and assigns the handle. When execution leaves the indented block for any reason — normal completion or a crash — Python calls `__exit__`, which closes the file. This is equivalent to wrapping file operations in a `try/finally` block and calling `f.close()` in `finally`. The `with` statement is syntactic sugar for exactly that pattern.

A file handle is closed the instant execution returns to the base indentation level after the `with` block. Any attempt to call `f.read()` or `f.write()` after the block raises `ValueError: I/O operation on closed file`. The file does not stay open — it is closed whether the block exited cleanly or crashed.

The dual context manager pattern opens two files in a single `with` statement using a comma: one for reading, one for writing. Both handles are guaranteed to close properly. This replaces the pattern of reading into a list, closing the input, then opening the output to write.

### The Tasks

#### Task 17.1: Verify the Auto-Close Behavior

1. Create `firewall_log.txt` with three fake log lines.
2. Open the file using a `with` block with `encoding="utf-8"` and assign the file object to `f`.
3. Inside the block, loop through the file and print each line.
4. After the `with` block ends — outside the indented block — print `f.closed`.
5. Confirm the output shows `True`.

#### Task 17.2: The Dual Context Manager (Read + Write)

1. Create `raw_alerts.txt` with at least five lines. Three lines must contain the word `CRITICAL`, two must not.
2. Open `raw_alerts.txt` for reading and `critical_only.txt` for writing in a single `with` statement using the comma syntax.
3. Loop through each line from the input file.
4. If the line contains `CRITICAL`, write it to the output file.
5. Add a counter that increments each time a line is written. Print the count after the block.

#### Task 17.3: Append vs Overwrite Under a Context Manager

1. Create a variable `alert_log_path` set to `"running_alerts.txt"`.
2. Open it in `"w"` mode and write `"Session started\n"`.
3. Open it in `"a"` mode and write `"Alert: 192.168.1.5 - port scan detected\n"`.
4. Open it in `"a"` mode again and write `"Alert: 10.0.0.2 - lateral movement\n"`.
5. Open it in `"r"` mode and print all contents.
6. Run the script twice. Observe what happens to the file on the second run. Add a comment explaining why the `"w"` block resets the file each time but the `"a"` blocks accumulate.

#### Task 17.4: Wrapping a Context Manager in a Function

1. Define a function `extract_errors` that takes `input_path` and `output_path` as parameters.
2. Inside the function, open both files in a single `with` statement.
3. Loop through each line in the input file. If the line contains `"ERROR"`, write it to the output and increment a counter.
4. Return only the count — not the path.
5. Create `system_log.txt` with a mix of `ERROR` and non-`ERROR` lines.
6. Call the function and print: `f"Processed evidence: {count} errors extracted to errors_only.txt"`.

### The Muscle Memory Gauntlet

**Mission: The Evidence Filter Pipeline**

I need to build a two-stage log processing pipeline using context managers throughout. The pipeline reads a raw IDS export, filters by severity, writes the matching lines to one output file, and writes the count to a summary file.

1. Create `ids_export.txt` using a `with` block in `"w"` mode. Write at least eight lines with a mix of `HIGH`, `CRITICAL`, `LOW`, and `MEDIUM` severities. Use realistic DFIR content — brute force attempts, lateral movement, Mimikatz execution, ransomware signatures.
2. Define a function `filter_high_severity` that takes `input_path`, `output_path`, and `summary_path` as parameters.
3. Inside the function, open `input_path` for reading and `output_path` for writing in a single `with` statement.
4. Loop through each line. If it contains `"HIGH"` or `"CRITICAL"`, write it to the output and increment a counter.
5. After the first `with` block closes, open `summary_path` for writing in a second `with` block.
6. Write a single line: `f"Total high-severity events: {count}\n"`.
7. Return the counter.
8. Call the function. Print the returned count to the terminal.
