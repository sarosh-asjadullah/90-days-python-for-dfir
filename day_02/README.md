Welcome to **Day 2**.

In [**Day 1**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_01), we learned how to capture evidence (Input) and display it (Output). Today, we learn how to **dissect** it.

In Digital Forensics, We almost never get clean data. We get a raw log line, a messy file path, or a jagged registry key. We need to be able to slice out exactly what We need—like a surgeon removing a bullet without damaging the surrounding tissue.

### Core Concept: The String is a List

Think of a string not as a word, but as a chain of individual characters. Each character has a "seat number" called an **Index**.

* **Positive Indexing:** Counts from the start (0, 1, 2...).
* **Negative Indexing:** Counts from the end (-1, -2...). This is critical for getting file extensions.
* **The Slicing Rule:** `[start : stop]`. **Crucial:** The "stop" index is *not* included in the result.

---

### The Mission: The Artifact Extractor

Create a new file in our repo: `day_02/string_drills.py`.

#### Task 2.1: The Extension Hunter (Negative Indexing)

In DFIR, we constantly check file extensions to spot executables disguised as documents.

1. Create a variable: `evidence_file = "suspicious_document.pdf.exe"`
2. Use **negative indexing** to slice just the last 3 characters.
3. Print it as: `Extension: exe`
4. **Drill:** Repeat this logic for `file_a = "config.ini"` and `file_b = "image.jpeg"` (Note: jpeg is 4 chars, how does our slice change?).

#### Task 2.2: The Path Normalizer (Sanitization)

Windows uses backslashes `\`. Linux and Python prefer forward slashes `/`. We must normalize paths to avoid errors.

1. Create a variable: `win_path = "C:\\Users\\Admin\\Downloads\\malware.tmp"` (Note: We use double backslashes `\\` because `\` is a special escape character in Python).
2. Convert the whole string to **lowercase** using `.lower()`.
3. Replace all `\` with `/` using `.replace("\\", "/")`.
4. Print the clean path.

#### Task 2.3: The Log Surgeon (Precision Slicing)

This is the most common task in scripting: parsing a fixed-format log.

* **The Log Line:** `"2024-01-26 14:30:00 [ERROR] Failed Login"`
* **The Mission:** Extract the specific parts using index numbers.
1. **Date:** First 10 chars (`2024-01-26`)
2. **Severity:** The text inside brackets (`ERROR`) - *Hint: We have to count the spaces!*
3. **Message:** The rest of the line (`Failed Login`)


* **Print format:** `Date: 2024-01-26 | Level: ERROR | Msg: Failed Login`

---

### The "Muscle Memory" Sprint (Do Not Skip)

To make this intuitive,We perform these rapid-fire drills. Type them, run them, delete them.

1. **The Reverse:**
* `s = "Digital Forensics"`
* Print it backwards using `print(s[::-1])`.


2. **The "Http" Check:**
* `url = "https://www.google.com"`
* Slice the first 5 characters. Does it equal "https"?


3. **The Step:**
* `hex_string = "1A2B3C4D"`
* Print every second character: `print(hex_string[::2])` (Result should be `1234`).



---
