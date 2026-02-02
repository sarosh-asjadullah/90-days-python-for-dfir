#TASK 2.1

evidence_file1 = "suspicious_documents.pdf.exe"
#print(evidence_file[-3:]) #Get the last N characters: Use text[-N:].Exclude the last N characters: Use text[:-N]. Slicing uses the format [start:stop:step]

evidence_file2 = "config.ini"
extension1 = evidence_file1[-3:]
print(f"Extension: {extension1}")

extension2 = evidence_file2[-3:]
print(f"Extension: {extension2}")

evidence_file3 = "image.jpeg"
extension3 = evidence_file3[-4:]
print(f"Extension: {extension3}")


#TASK 2.2

win_path = "C:\\Users\\Admin\\Downloads\\malware.tmp"
win_path_lower = win_path.lower()
clean_path = win_path_lower.replace("\\","/")
print(clean_path)

#TASK 2.3

log_line = "2024-01-26 14:30:00 [ERROR] Failed Login"
date = log_line[0:11].strip()
severity = log_line[21:26].strip()
message = log_line[27:].strip() #For fixed headers (like timestamps and severity levels at the start of a log), use Positive Indexing (counting from the start).
print(f"Date: {date} | Level: {severity} | Msg: {message}")

s = "Digital Forensics"
print(s[::-1])  #Reverse the string - A negative step value in a slice will print the string in reverse

url = "https://www.google.com"
proto = url[:5]
if proto == "https":
    print("The Protocol is HTTPS")

hex_string = "1A2B3C4D"
print(hex_string[1::2]) # Start at index 1 ('A'), go to the end, jump by 2 - Prints ABCD
print(hex_string[::2]) # Start at index 0 ('1'), go to the end, jump by 2 - Prints 1234
