## Day 4: The Repeater (Lists & Loops)

This is the day everything changes. Until now, I’ve handled one IP or one file at a time. Real forensics involves thousands.

I want **heavy repetition** on this. I’m going to drill the concept of **iteration** (looping) until I dream in `for` loops.

### Core Concepts

1. **The List:** A collection of items. `suspects = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]`
    
2. **The Loop:** A machine that grabs items one by one. `for ip in suspects:`
    
3. **The Block:** The code inside the loop that runs for _every single item_.
    

---

### The Task: The Mass Scanner

Create `day_04/loop_drills.py`.

#### Drill 4.1: The Roll Call (Basic Iteration)

- **Goal:** Run code once for every item in a list.
    
- **Code:**
    
    1. Create a list: `ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]`
        
    2. Write a loop:
        
        ```python
        for ip in ip_list:
            print(f"Scanning IP: {ip}")
        ```
        
    3. _Notice:_ The variable `ip` (I could call it `x`, `item`, `target`) is a temporary placeholder that changes every time the loop runs.
        

#### Drill 4.2: The Filter (Loop + If)

- **Goal:** This is the most common pattern in Python: loop through data, check a condition, act on it.
    
- **Code:**
    
    1. `ports = [80, 443, 22, 21, 8080]`
        
    2. Loop through the list.
        
    3. **Inside the loop**:
        
        - If the port is `22`: print `"SSH detected on port 22"`
            
        - Else: `print(f"Port {port} is standard")`
            

#### Drill 4.3: The Accumulator (Counting)

- **Goal:** Count how many times something happens.
    
- **Code:**
    
    1. `log_statuses = ["Success", "Failed", "Success", "Failed", "Failed", "Success"]`
        
    2. Create a counter variable _outside_ the loop: `failed_count = 0`
        
    3. Loop through `log_statuses`.
        
    4. **Inside the loop:** If the status is `"Failed"`, add 1 to the counter: `failed_count = failed_count + 1`
        
    5. **Outside the loop (at the end):** Print `f"Total failed logins: {failed_count}"`
        

---

### The “Muscle Memory” Repetition

This is where I lock it in.

**The “Search & Destroy” Drill:**

1. Write a list of filenames: `files = ["cmd.exe", "report.docx", "powershell.exe", "notes.txt"]`
    
2. Write a loop that checks:
    
    - If the file ends with `".exe"`, print `"Suspicious executable found: <filename>"`
        
    - Otherwise, `pass` (do nothing).
        

**Constraint:**

Write this code. Run it. Delete it.

Write it again, but this time look for `".docx"`.

Write it again, but count how many `.exe` files there are (using the logic from Drill 4.3).
