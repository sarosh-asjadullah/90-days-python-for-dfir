# Python for DFIR — 90-Day Apprenticeship

This repository documents a 90-day, exercise-driven journey to build **practical Python proficiency for Digital Forensics and Incident Response (DFIR)**.

The focus is not on learning Python syntax in isolation, but on developing **muscle memory** and **analyst-style thinking** through small, repeatable, real-world tasks.

---

## Philosophy

- One focused task per day  
- Every task produces a **working, reviewable artifact**
- No filler, no copy-paste exercises
- Emphasis on correctness, clarity, and deterministic output
- DFIR mindset from Day 1 (text, logs, artifacts, structure)

This mirrors how DFIR skills are built in practice: incrementally, deliberately, and with attention to detail.

---

## What This Demonstrates

By the end of this series, this repository will show:

- Progressive Python skill development
- Comfort with strings, files, control flow, and data structures
- Ability to translate investigative logic into code
- Consistent delivery and version control discipline
- Practical foundations for DFIR automation and tooling

---

## Progress Tracking
- [ ] Phase 1: The Scripter (Days 1-30) - **In Progress**
- [ ] Phase 2: The Automator (Days 31-60)
- [ ] Phase 3: The Analyst (Days 61-90)

## Day 1: The Interrogation (Input/Output)
**Goal:** Master variable assignment, user input, and formatted output.

### Day 1: Learning Reflections
- **Technical Progress:** Learned to capture user input, use f-strings for reporting, and sanitize strings with `.strip()`.
- **Logic Insight:** Confirmed that `input()` defaults to string data even if I intend to use it as a number.
- **Muscle Memory:** Practiced the `f"[TAG] {variable}"` pattern which is the bread and butter of log generation.

### Exercises Completed:
1. **triage_report.py**: Captures Analyst name, Case ID, and Target IP.
2. **variable_swap.py**: Practicing re-assignment of network configurations.
3. **evidence_string.py**: Building alert strings from multiple data types.

## Day 2: String Slicing & Methods
- **Technical Progress:** Mastered slicing `[start:stop]`, negative indexing `[-n]`, and sanitization methods (`.lower()`, `.replace()`).
- **Logic Insight:** The "Stop" index is exclusive. To get characters 0-4, I must type `[0:5]`.
- **Scar Tissue:** Escape characters! I learned that `\` inside a string needs to be written as `\\`.

## Day 3: Logic & Control Flow
- **Technical Progress:** Learned `if`, `elif`, `else`, comparators (`==`, `!=`, `>`), and the powerful `in` operator.
- **Logic Insight:** Python evaluates conditionals top-to-bottom. The first expression that evaluates to `True` wins, and the rest are ignored. Order matters!
- **Muscle Memory:** Practiced compound logic (`and`/`or`) to create "Kill Chain" rules for flagging threats.

## Day 4: Lists & Loops
- **Technical Progress:** Mastered the `for` loop to iterate through lists. Learned the "Accumulator Pattern" (counters) to summarize data.
- **Logic Insight:** A loop repeats the *same* block of code for *different* data items. Variables defined outside the loop (like counters) persist and grow; variables inside the loop reset on every iteration.
- **Muscle Memory:** Combined `if` statements inside `for` loops to create filters (Search & Destroy).

## Day 5: Lists & Dictionaries
- **Technical Progress:** Learned to dynamically build lists using `.append()`. Mastered Dictionary lookups (`key -> value`).
- **Logic Insight:** - Lists (`[]`) are for ordered items (logs, files).
    - Dictionaries (`{}`) are for mapping data (IP->Country, Port->Protocol).
    - `KeyError` happens when asking a dictionary for a key that doesn't exist.
- **Muscle Memory:** Combined loops with `if` statements to filter data into new lists.
