Welcome to **Day 13**.

In [**Day 12**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_12), I explored Lists vs. Tuples vs. Sets and learned how Set operations can instantly deduplicate and filter data. Today, I learn how to make my scripts **dynamic** from the command line.

Until now, every script I have written is "locked." To scan a different file, I open the code, change the variable, save, and run. During a live incident, that is unacceptable. I need tools that accept instructions at launch — like turning a fixed screwdriver into a power drill that accepts different bits depending on the job.

### Core Concept: `sys.argv` (Command Line Arguments)

When I type `python scanner.py evidence.log 443` in the terminal, Python captures everything into a list called `sys.argv`.

- **`sys.argv[0]`** is always the script name. I almost never use it.
- **`sys.argv[1]`** is the first real argument.
- **`sys.argv[2]`** is the second real argument.
- **Every item is a string**, even if it looks like a number.
- **`len(sys.argv)`** tells me how many items were provided.
- **`sys.exit()`** kills the script immediately when validation fails.

---

### The Tasks: Command Line Mastery

I created a new file in my repo: `day_13/cli_tool.py`.

#### Task 13.1: The Argument Echo

I need to see exactly what Python receives from the terminal.

1. Import `sys`.
2. Print the entire `sys.argv` list.
3. Print the total number of arguments using `len()`.

I ran it three ways:

- `python cli_tool.py`
- `python cli_tool.py hello`
- `python cli_tool.py 192.168.1.1 443 scan`

I observed how the list grows with each run.

#### Task 13.2: The Guard Rail (Input Validation)

I need to prevent a crash when the user forgets to provide an argument.

1. Import `sys`.
2. If the total number of arguments is less than 2, print `"Usage: python cli_tool.py <target_ip>"` and exit the script.
3. Otherwise, store argument 1 in a variable called `target`.
4. Print `"Commencing scan on: {target}"`.

**Muscle Memory:** I ran it with no arguments first — watched the usage message. Then ran it with an IP. Deleted the code. Wrote it again without looking.

#### Task 13.3: The File Loader (Dynamic File Opening)

I need to accept a filename from the terminal and print its contents line by line.

1. Import `sys`.
2. Validate that at least one argument was provided. If not, print usage and exit.
3. Store argument 1 as `filename`.
4. Use a `try` block to open the file and loop through its lines. Strip and print each line.
5. Use an `except FileNotFoundError` block to print an error message if the file does not exist.

I ran it: `python cli_tool.py suspicious_ips.txt`

This single script can now open **any** file without editing a single line of code.

---

### The "Muscle Memory" Gauntlet (The Dynamic Hunter)

This is the combination drill. I am merging [**Day 7**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_07) (Log Parsing) with Day 13 (CLI Arguments).

**The Mission:** I built a script (`hunter.py`) that takes a filename and a keyword from the command line and counts how many lines in that file contain the keyword.

1. Import `sys`.
2. If the total number of arguments is not exactly 3, print `"Usage: python hunter.py <filename> <keyword>"` and exit.
3. Store argument 1 as `filename` and argument 2 as `keyword`.
4. Create a counter variable set to 0.
5. Use a `try` block to open the file for reading.
6. Loop through every line. Strip the line. If the keyword is found in the line, increment the counter.
7. Use an `except FileNotFoundError` to handle missing files.
8. After the loop, print `"Found {count} instances of '{keyword}' in {filename}"`.

I ran it: `python hunter.py access.log /admin`

Expected output: `Found 2 instances of '/admin' in access.log`

(I used the `access.log` I created on Day 7.)