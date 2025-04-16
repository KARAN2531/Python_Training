'''
4. Log File Filter
A log file contains lines with different severity levels (INFO, WARNING, ERROR). Write a program that extracts all ERROR messages and saves them in a separate file.
'''

def log_file_filter(log_file, filter_file):
    with open(log_file, "r", encoding="utf-8") as log,  open(filter_file, "w", encoding="utf-8") as fil:
        for line in log:
            if "ERROR" in line:
                fil.write(line)

log_file = r"File_IO_Problems\Log_file_filter\log.txt"
filter_file = r"File_IO_Problems\Log_file_filter\filter.txt"

log_file_filter(log_file, filter_file)
print(f"All error message extractedd to {filter_file}")