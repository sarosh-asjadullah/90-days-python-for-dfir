Welcome to **Day 1**. Today is about the most fundamental interaction: **Input, Storage, and Output.** In DFIR, everything starts with an "artifact" (a piece of data). Before we can analyze it, we have to know how to hold it in memory and display it.

### Concepts for Today

1. **Variables:** Think of these as evidence bags. You give them a label (name) and put data inside.
2. **Strings:** These are text-based data (like an IP address or a username). They must be inside quotes: `"192.168.1.1"`.
3. **The `print()` function:** This is how your script "speaks" back to you.
4. **The `input()` function:** This is how you interrogate a user to get information.

---

### The Task: The "First Responder" Triage Script

You are going to write a script that collects basic incident information from an analyst and prints a summary report. This seems simple, but you are going to do it **multiple times** with variations to build that muscle memory.

#### Task 1.1: The Standard Report

Write a script that asks for:

* The Analyst's Name
* The Case Number
* The Target IP Address

Then, print it out in this exact format:
`[REPORT] Analyst: <name> | Case: <number> | Target: <ip>`

#### Task 1.2: The "Variable Swap" Drill

Create two variables: `primary_dns = "8.8.8.8"` and `secondary_dns = "1.1.1.1"`.

1. Print them both.
2. Now, re-assign them. Change `primary_dns` to "9.9.9.9" and `secondary_dns` to "8.8.4.4".
3. Print them again.
*Goal: Understand that variables are "variable"—they can change.*

#### Task 1.3: The "Evidence String" Drill

Create three variables:

* `protocol = "HTTPS"`
* `port = 443` (Note: No quotes for numbers!)
* `status = "Malicious"`

Combine them into one single string variable called `alert_message` and print it. It should look like: `ALERT: HTTPS traffic on port 443 is Malicious`.

---

### How to do this for "Muscle Memory"

1. **Do not copy-paste.** Open your IDE (VS Code, PyCharm, or even a text editor).
2. **Type it from scratch.**
3. **Delete the code and do it again.** Do Task 1.1 three times without looking at your previous attempt.
4. **Deliberate Error:** Try to print a variable you haven't created yet. See the `NameError`. Remember it.

---

