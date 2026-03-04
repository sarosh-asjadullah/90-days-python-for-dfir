import sys
def file_read(filename,keyword):
    counter = 0
    try:
        with open (filename,"r",encoding="utf-8",errors="ignore") as f:
            for lines in f:
                if keyword in lines:
                    counter = counter+1
            print(f"Found {counter} instances of {keyword} in {filename}")
    except FileNotFoundError:
        print(f"{filename} is not found")

if len(sys.argv) < 3:
    print("Usage: python hunter.py <filename> <keyword>")
    sys.exit()
file_read(sys.argv[1],sys.argv[2])

