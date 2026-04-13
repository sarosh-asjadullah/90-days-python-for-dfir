Welcome to **Day 16**.

In [**Day 15**](https://github.com/sarosh-asjadullah/90-days-python-for-dfir/tree/main/day_15), I learned to read and write structured CSV data using `csv.reader`, `csv.DictReader`, and `csv.writer`. Today, I move to the other universal data format: **JSON**.

CSV is a table. JSON is a tree. In DFIR, I encounter JSON everywhere — API responses from VirusTotal and AbuseIPDB, cloud logs from AWS CloudTrail, Splunk query exports, and EDR telemetry from CrowdStrike or Cortex XDR. If CSV is a spreadsheet, JSON is a nested filing cabinet — drawers inside drawers inside drawers.

### Core Concepts

- **`json.load(file)`**: Reads a JSON **file** and converts it into a Python dictionary or list.
- **`json.loads(string)`**: Reads a JSON **string** and converts it. (The `s` stands for "string.")
- **`json.dump(data, file)`**: Writes a Python dictionary/list to a **file** as JSON.
- **`json.dumps(data)`**: Converts a Python dictionary/list to a JSON **string**.
- **`indent=4`**: Makes the output human-readable instead of one giant line.

The mapping is direct: JSON objects `{}` become Python dictionaries. JSON arrays `[]` become Python lists. JSON strings become Python strings. JSON numbers become Python ints or floats.

---

### The Setup

I created two dummy files in my `day_16` folder.

**`alert.json`** — A single alert object with nested source/destination data and an indicators list.

**`multi_alerts.json`** — A JSON array containing multiple alert objects, each with severity, source/destination IPs, and action taken.

---

### The Tasks

I created `day_16/json_drills.py`.

#### Task 16.1: The Loader (Reading JSON)

1. Import `json`.
2. Open `alert.json` for reading.
3. Load the data: `data = json.load(file)`.
4. Print the entire `data` variable and observe it is a `dict`.

#### Task 16.2: The Deep Dive (Accessing Nested Data)

1. Print the alert ID: `data["alert_id"]`.
2. Print the source IP: `data["source"]["ip"]` — a dictionary inside a dictionary.
3. Print the destination country: `data["destination"]["country"]`.
4. Loop through the indicators list and print each IOC.

#### Task 16.3: The Filter (Processing a JSON Array)

1. Open `multi_alerts.json` and load it — this time `data` is a **list** of dictionaries.
2. Loop through the list.
3. If the alert's severity is `"HIGH"` or `"CRITICAL"`, print the alert_id and source_ip.

#### Task 16.4: The Writer (Creating JSON Output)

1. From the `multi_alerts.json` data, collect all alerts where action is `"blocked"` into a new list.
2. Write the list to `blocked_alerts.json` using `json.dump()` with `indent=4`.
3. Verify the output file looks like proper, readable JSON.

---

### The "Muscle Memory" Gauntlet (The Alert Summarizer)

**The Mission:** I built a script that reads `multi_alerts.json` and produces a structured summary report as a new JSON file.

The output file `summary.json` has this structure:

```json
{
    "total_alerts": "<total count>",
    "severity_breakdown": {
        "HIGH": "<count>",
        "CRITICAL": "<count>",
        "LOW": "<count>"
    },
    "blocked_ips": ["<list of unique destination IPs that were blocked>"]
}
```

1. Open and load `multi_alerts.json`.
2. Create a dictionary to count severities (same counter pattern from Day 15).
3. Create a list to collect destination IPs where action is `"blocked"`. Deduplicate using `set()`.
4. Build the summary dictionary with the three keys shown above.
5. Write it to `summary.json` with `indent=4`.