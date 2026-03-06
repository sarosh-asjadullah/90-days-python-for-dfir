import sys

def main():
    print(sys.argv)
    print_on_screen = False
    unique_flag = False
    if "--unique" in sys.argv:
        unique_flag = True
    if "--verbose" in sys.argv:
        print_on_screen = True
    
    if len(sys.argv) < 3:
        print(f"Usage : python log_analyzer.py <filename> <keyword> --unique(optional) --verbose(optional)")
        sys.exit()

    else:
        result = analyze_log(sys.argv[1],sys.argv[2],unique_flag)
    print(result)
    write_report(result,sys.argv[1],sys.argv[2],print_on_screen)
    print("Report saved to report.txt")



def write_report(ip_list,filename,keyword,print_on_screen = False):
    counter = 1
    with open ("report.txt","w",encoding="utf-8",errors="ignore") as file_write:
        header = f"--- LOG ANALYSIS REPORT ---\n"
        target = f"The {filename} analyzed for keyword: {keyword}\n"
        total = f"The total count of IPs found is: {len(ip_list)}\n"

        file_write.write(header)
        file_write.write(target)
        file_write.write(total)

        if print_on_screen == True:
            print(header)
            print(target)
            print(total)
        
        for ip in ip_list:
            line = f"{counter}. {ip}"
            file_write.write(f"{line}\n")
            if print_on_screen:
                print(line)
            counter += 1

def analyze_log(filename,keyword,unique_flag=False):
    split_line =[]
    ip_list = []
    try:
        with open(filename,"r",encoding="utf-8",errors="ignore") as file:
            for line in file:
                if keyword in line:
                    split_line = line.split()
                    ip_list.append(split_line[0])
    except FileNotFoundError:
        print(f"Error:{filename} is not found.")
        sys.exit()
    if unique_flag == True:
        ip_set = set(ip_list)
        sorted_ip_list = sorted(ip_set)
        return sorted_ip_list
    else:
        return ip_list


main()

                    
