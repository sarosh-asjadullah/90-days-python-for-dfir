Welcome to **Day 14**.

In [**Day 13**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_13), I learned how to make my scripts dynamic using `sys.argv` to accept command line arguments. Today is a **Capstone Day** — no new concepts. I am combining everything from Days 8 through 13 into a single, professional command-line tool.

Think of it like this: Days 1-7 taught me individual martial arts moves. Days 8-13 taught me combinations. Today I step into the ring and fight a full round.

### The Mission: The CLI Log Analyzer

I built a CLI tool (`log_analyzer.py`) that accepts a log file and an optional flag, then produces a structured report. This is the kind of script a senior analyst hands to a junior and says "run this against the evidence."

---

### The Tool: `log_analyzer.py`

The script accepts 2 or 3 arguments from the command line:

- **Argument 1:** The log file to analyze (e.g., `access.log`)
- **Argument 2:** The keyword to hunt for (e.g., `/admin`)
- **Argument 3 (optional):** `--unique` flag. If present, only report unique IPs.

**Execution examples:**

- `python log_analyzer.py access.log /admin`
- `python log_analyzer.py access.log /admin --unique`

---

### The Requirements

#### Step 1 — Validation

- If fewer than 3 arguments are provided, print a usage message and exit.
- If the file does not exist, print an error and exit.

#### Step 2 — Core Logic (Function: `analyze_log`)

- I defined a function called `analyze_log` that accepts the filename and the keyword.
- Inside the function, I open the file and loop through every line.
- If the keyword is found in the line, I extract the IP address (first element after splitting by space).
- I store matching IPs in a list and return it.

#### Step 3 — Deduplication (Conditional)

- I check if `--unique` was passed as the third argument.
- If yes, I convert the IP list to a set, then back to a sorted list.
- If no, I keep the full list as-is.

#### Step 4 — Reporting (Function: `write_report`)

- I defined a function called `write_report` that accepts the list of IPs, the keyword, and the filename.
- I open a new file called `report.txt` in write mode.
- I write a header line: `--- LOG ANALYSIS REPORT ---`
- I write the target file and keyword searched.
- I write the total count of IPs found.
- I loop through the IP list and write each one as a numbered entry.

#### Step 5 — Execution

- I call `analyze_log` with the CLI arguments.
- I apply deduplication if the flag is present.
- I call `write_report` with the results.
- I print a confirmation: `"Report saved to report.txt"`

---

### The "Muscle Memory" Gauntlet

After completing the main tool, I added one more feature:

- A `--verbose` flag. If present, each matching line is printed to the terminal as it is found, in addition to writing the report. If not present, the script runs silently and only produces the file.

---

### Skills to be Combined in This Milestone

| Day | Skill | How I Used It |
|-----|-------|---------------|
| 8 | Functions | `analyze_log()` and `write_report()` |
| 9 | Error Handling | `try/except` for missing files |
| 10 | OS Module | `os.path.exists()` for file validation "Note - Didnt use this" | 
| 11 | String Splitting | `.split(" ")` to extract IPs from log lines |
| 12 | Sets | `set()` for deduplication with `--unique` |
| 13 | sys.argv | CLI arguments for filename, keyword, and flags |